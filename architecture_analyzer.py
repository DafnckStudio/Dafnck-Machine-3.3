#!/usr/bin/env python3
"""
Architecture Analyzer Script
Analyzes folder structure, extracts YAML front matter, and displays markdown file architecture.
"""

import os
import sys
import re
import yaml
import json
import csv
import argparse
import signal
import tempfile
import atexit
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel
from rich.text import Text

@dataclass
class FileAnalysis:
    """Data class to store file analysis results."""
    filename: str
    filepath: str
    yaml_frontmatter: Optional[Dict[str, Any]]
    headers: List[str]
    yaml_valid: bool
    yaml_errors: List[str]
    missing_required_fields: List[str]

class ArchitectureAnalyzer:
    """Main analyzer class for folder architecture."""
    
    # Required YAML fields for validation
    REQUIRED_YAML_FIELDS = [
        'phase', 'step', 'task', 'task_id', 'title', 
        'previous_task', 'next_task', 'version', 'agent', 'orchestrator'
    ]
    
    # Class variable to track temporary files for cleanup
    _temp_files = []
    
    def __init__(self, folder_path: str, recursive: bool = False, show_structure: bool = False, 
                 export_format: Optional[str] = None, output_dir: str = "./exports", export_html: bool = False):
        """Initialize analyzer with folder path."""
        self.folder_path = Path(folder_path)
        self.console = Console()
        self.files_analysis: List[FileAnalysis] = []
        self.recursive = recursive
        self.show_structure = show_structure
        self.export_format = export_format
        self.output_dir = Path(output_dir)
        self.analysis_timestamp = datetime.now()
        self.export_html = export_html
        self.temp_html_file = None
        
        if not self.folder_path.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        if not self.folder_path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {folder_path}")
        
        # Create output directory if exporting
        if self.export_format:
            self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup signal handlers for cleanup
        if self.export_html:
            signal.signal(signal.SIGINT, self._signal_handler)
            signal.signal(signal.SIGTERM, self._signal_handler)
            atexit.register(self._cleanup_temp_files)
    
    @classmethod
    def _cleanup_temp_files(cls):
        """Clean up temporary files."""
        for temp_file in cls._temp_files:
            try:
                if temp_file.exists():
                    temp_file.unlink()
            except Exception:
                pass
        cls._temp_files.clear()
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signals for cleanup."""
        self.console.print("\n\n🧹 [yellow]Cleaning up temporary files...[/yellow]")
        self._cleanup_temp_files()
        self.console.print("✅ [green]Cleanup completed. Goodbye![/green]")
        sys.exit(0)
    
    def export_html_interactive(self) -> str:
        """Export to HTML file in current directory and return file path."""
        # Create HTML file in current working directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"architecture_analysis_{timestamp}.html"
        temp_file = Path.cwd() / filename
        
        # Track for cleanup
        self.__class__._temp_files.append(temp_file)
        self.temp_html_file = temp_file
        
        # Generate HTML content
        html_content = self._generate_html_content()
        
        # Write to file
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(temp_file)
    
    def _generate_html_content(self) -> str:
        """Generate HTML content for export."""
        export_data = self.get_export_data()
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Analysis Report - Interactive</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
        h1, h2, h3 {{ color: #333; }}
        h1 {{ text-align: center; color: #4a5568; margin-bottom: 30px; }}
        .metadata {{ background: linear-gradient(135deg, #e8f4fd 0%, #d6eaf8 100%); padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #3498db; }}
        .summary {{ background: linear-gradient(135deg, #f0f8f0 0%, #e8f5e8 100%); padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #27ae60; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 25px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); font-weight: 600; color: #495057; }}
        .valid {{ color: #27ae60; font-weight: bold; }}
        .invalid {{ color: #e74c3c; font-weight: bold; }}
        .file-details {{ margin-bottom: 25px; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: #fafafa; }}
        .headers {{ background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; }}
        .errors {{ background: #f8d7da; padding: 15px; border-radius: 8px; border-left: 4px solid #dc3545; }}
        .missing {{ background: #f8d7da; padding: 15px; border-radius: 8px; border-left: 4px solid #dc3545; }}
        .timestamp {{ font-size: 0.9em; color: #666; text-align: center; margin-top: 20px; }}
        .refresh-note {{ background: #e1f5fe; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #03a9f4; }}
        tr:nth-child(even) {{ background-color: #f8f9fa; }}
        tr:hover {{ background-color: #e3f2fd; }}
    </style>
    <script>
        // Auto-refresh every 30 seconds if the file is updated
        setTimeout(function() {{
            location.reload();
        }}, 30000);
    </script>
</head>
<body>
    <div class="container">
        <h1>📊 Architecture Analysis Report (Interactive)</h1>
        
        <div class="refresh-note">
            <strong>🔄 Auto-refresh:</strong> This page will automatically refresh every 30 seconds to show updates.
            <br><strong>🛑 Stop:</strong> Press Ctrl+C in the terminal to stop the analysis and clean up this file.
        </div>
        
        <div class="metadata">
            <h2>📋 Analysis Metadata</h2>
            <p><strong>Timestamp:</strong> {export_data['analysis_metadata']['timestamp']}</p>
            <p><strong>Folder Path:</strong> {export_data['analysis_metadata']['folder_path']}</p>
            <p><strong>Recursive Analysis:</strong> {export_data['analysis_metadata']['recursive']}</p>
            <p><strong>Total Files:</strong> {export_data['analysis_metadata']['total_files']}</p>
        </div>
        
        <div class="summary">
            <h2>📈 Summary</h2>
            <p><strong>Valid Files:</strong> <span class="valid">{export_data['analysis_metadata']['valid_files']}</span></p>
            <p><strong>Invalid Files:</strong> <span class="invalid">{export_data['analysis_metadata']['invalid_files']}</span></p>
            <p><strong>Success Rate:</strong> {(export_data['analysis_metadata']['valid_files']/export_data['analysis_metadata']['total_files']*100):.1f}%</p>
            <p><strong>Total Headers:</strong> {sum(len(file['headers']) for file in export_data['files'])}</p>
        </div>
        
        <h2>📁 Files Analysis</h2>
        <table>
            <thead>
                <tr>
                    <th>File</th>
                    <th>Status</th>
                    <th>Headers</th>
                    <th>Missing Fields</th>
                    <th>Errors</th>
                </tr>
            </thead>
            <tbody>"""
        
        for file_data in export_data['files']:
            status_class = "valid" if file_data['yaml_valid'] else "invalid"
            status_icon = "✅ Valid" if file_data['yaml_valid'] else "❌ Invalid"
            
            html_content += f"""
                <tr>
                    <td>{file_data['filename']}</td>
                    <td class="{status_class}">{status_icon}</td>
                    <td>{len(file_data['headers'])}</td>
                    <td>{len(file_data['missing_required_fields'])}</td>
                    <td>{len(file_data['yaml_errors'])}</td>
                </tr>"""
        
        html_content += """
            </tbody>
        </table>
        
        <h2>🔄 Workflow Dependency Schema</h2>"""
        
        # Generate workflow dependency diagram
        workflow_html = self._generate_workflow_schema_html(export_data['files'])
        html_content += workflow_html
        
        html_content += """
        <h2>📝 Detailed File Analysis</h2>"""
        
        # Add detailed analysis for each file
        for file_data in export_data['files']:
            status_class = "valid" if file_data['yaml_valid'] else "invalid"
            status_icon = "✅ Valid" if file_data['yaml_valid'] else "❌ Invalid"
            
            html_content += f"""
        <div class="file-details">
            <h3>📄 {file_data['filename']}</h3>
            <p><strong>Path:</strong> {file_data['filepath']}</p>
            <p><strong>YAML Valid:</strong> <span class="{status_class}">{status_icon}</span></p>"""
            
            # Add YAML front matter details
            if file_data['yaml_frontmatter']:
                html_content += """
            <div class="headers">
                <h4>📋 YAML Front Matter</h4>
                <ul>"""
                for key, value in file_data['yaml_frontmatter'].items():
                    is_required = key in export_data['summary']['required_yaml_fields']
                    field_status = "✅" if is_required else "ℹ️"
                    html_content += f"<li>{field_status} <strong>{key}:</strong> {value}</li>"
                html_content += "</ul></div>"
            
            # Add headers
            if file_data['headers']:
                html_content += f"""
            <div class="headers">
                <h4>📝 Headers ({len(file_data['headers'])})</h4>
                <ul>{''.join(f'<li>• {header}</li>' for header in file_data['headers'])}</ul>
            </div>"""
            else:
                html_content += "<p>No headers found</p>"
            
            # Add missing fields
            if file_data['missing_required_fields']:
                html_content += f"""
            <div class="missing">
                <h4>❌ Missing Required Fields ({len(file_data['missing_required_fields'])})</h4>
                <ul>{''.join(f'<li>{field}</li>' for field in file_data['missing_required_fields'])}</ul>
            </div>"""
            
            # Add YAML errors
            if file_data['yaml_errors']:
                html_content += f"""
            <div class="errors">
                <h4>⚠️ YAML Errors ({len(file_data['yaml_errors'])})</h4>
                <ul>{''.join(f'<li>{error}</li>' for error in file_data['yaml_errors'])}</ul>
            </div>"""
            
            html_content += "</div>"
        
        html_content += """
        <div class="timestamp">
            Generated at: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    
    def _generate_workflow_schema_html(self, files_data: List[Dict]) -> str:
        """Generate HTML for workflow dependency schema."""
        workflow_html = """
        <div class="workflow-container">
            <div class="workflow-legend">
                <h3>🗺️ Task Flow Diagram</h3>
                <p>Shows the dependency relationships between tasks based on <code>previous_task</code> and <code>next_task</code> fields.</p>
            </div>
            <style>
                .workflow-container { margin-bottom: 30px; }
                .workflow-legend { background: #e8f4fd; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #3498db; }
                .workflow-diagram { background: white; border: 2px solid #ddd; border-radius: 10px; padding: 20px; overflow-x: auto; }
                .workflow-phase { margin-bottom: 25px; }
                .phase-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 10px 15px; border-radius: 6px; font-weight: bold; margin-bottom: 15px; }
                .task-flow { display: flex; flex-wrap: wrap; gap: 15px; align-items: center; margin-bottom: 10px; }
                .task-node { background: #f8f9fa; border: 2px solid #dee2e6; border-radius: 8px; padding: 10px 15px; min-width: 200px; text-align: center; position: relative; }
                .task-node.valid { border-color: #28a745; background: #d4edda; }
                .task-node.invalid { border-color: #dc3545; background: #f8d7da; }
                .task-id { font-weight: bold; color: #495057; }
                .task-title { font-size: 0.9em; color: #6c757d; margin-top: 5px; }
                .task-agent { font-size: 0.8em; color: #007bff; margin-top: 3px; }
                .flow-arrow { font-size: 1.5em; color: #6c757d; margin: 0 10px; }
                .orphan-tasks { margin-top: 20px; }
                .orphan-header { background: #ffc107; color: #212529; padding: 8px 12px; border-radius: 6px; font-weight: bold; margin-bottom: 10px; }
                .workflow-stats { background: #f8f9fa; padding: 15px; border-radius: 8px; margin-top: 20px; }
                .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; }
                .stat-item { text-align: center; }
                .stat-number { font-size: 1.5em; font-weight: bold; color: #495057; }
                .stat-label { font-size: 0.9em; color: #6c757d; }
            </style>
            <div class="workflow-diagram">"""
        
        # Build workflow data structure
        workflow_data = self._build_workflow_data(files_data)
        
        # Generate phase-based workflow
        for phase, tasks in workflow_data['phases'].items():
            workflow_html += f"""
                <div class="workflow-phase">
                    <div class="phase-header">📋 Phase {phase}</div>"""
            
            # Group tasks by step within phase
            steps = {}
            for task in tasks:
                step = task.get('step', 'Unknown')
                if step not in steps:
                    steps[step] = []
                steps[step].append(task)
            
            for step, step_tasks in sorted(steps.items()):
                if len(step_tasks) > 1:
                    workflow_html += f"""
                    <div style="margin-bottom: 15px;">
                        <strong>Step {step}:</strong>
                        <div class="task-flow">"""
                    
                    for i, task in enumerate(step_tasks):
                        if i > 0:
                            workflow_html += '<span class="flow-arrow">→</span>'
                        workflow_html += self._generate_task_node_html(task)
                    
                    workflow_html += "</div></div>"
                else:
                    task = step_tasks[0]
                    workflow_html += f"""
                    <div style="margin-bottom: 10px;">
                        <strong>Step {step}:</strong>
                        <div class="task-flow">{self._generate_task_node_html(task)}</div>
                    </div>"""
            
            workflow_html += "</div>"
        
        # Show orphaned tasks (tasks without proper connections)
        if workflow_data['orphaned']:
            workflow_html += """
                <div class="orphan-tasks">
                    <div class="orphan-header">⚠️ Orphaned Tasks (No Clear Dependencies)</div>
                    <div class="task-flow">"""
            
            for task in workflow_data['orphaned']:
                workflow_html += self._generate_task_node_html(task)
            
            workflow_html += "</div></div>"
        
        # Add workflow statistics
        workflow_html += f"""
                <div class="workflow-stats">
                    <h4>📊 Workflow Statistics</h4>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['total_tasks']}</div>
                            <div class="stat-label">Total Tasks</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['connected_tasks']}</div>
                            <div class="stat-label">Connected Tasks</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['orphaned_tasks']}</div>
                            <div class="stat-label">Orphaned Tasks</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['phases_count']}</div>
                            <div class="stat-label">Phases</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['valid_tasks']}</div>
                            <div class="stat-label">Valid Tasks</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">{workflow_data['stats']['completion_rate']:.1f}%</div>
                            <div class="stat-label">Completion Rate</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
        
        return workflow_html
    
    def _build_workflow_data(self, files_data: List[Dict]) -> Dict:
        """Build workflow data structure from files."""
        phases = {}
        orphaned = []
        valid_tasks = 0
        connected_tasks = 0
        
        # Process each file to extract workflow information
        for file_data in files_data:
            if not file_data['yaml_valid'] or not file_data['yaml_frontmatter']:
                continue
                
            yaml_data = file_data['yaml_frontmatter']
            
            # Extract task information
            task_info = {
                'filename': file_data['filename'],
                'task_id': yaml_data.get('task_id', 'Unknown'),
                'title': yaml_data.get('title', 'Unknown'),
                'phase': yaml_data.get('phase', 'Unknown'),
                'step': yaml_data.get('step', 'Unknown'),
                'agent': yaml_data.get('agent', 'Unknown'),
                'previous_task': yaml_data.get('previous_task', None),
                'next_task': yaml_data.get('next_task', None),
                'valid': file_data['yaml_valid']
            }
            
            if task_info['valid']:
                valid_tasks += 1
            
            # Check if task has connections
            if task_info['previous_task'] or task_info['next_task']:
                connected_tasks += 1
            
            # Group by phase
            phase = task_info['phase']
            if phase not in phases:
                phases[phase] = []
            phases[phase].append(task_info)
        
        # Find orphaned tasks (tasks that don't connect properly)
        all_task_ids = {task['task_id'] for phase_tasks in phases.values() for task in phase_tasks}
        
        for phase_tasks in phases.values():
            for task in phase_tasks:
                # Check if previous_task and next_task references exist
                prev_exists = not task['previous_task'] or task['previous_task'] in all_task_ids or task['previous_task'].startswith('PHASE')
                next_exists = not task['next_task'] or task['next_task'] in all_task_ids or task['next_task'].startswith('P')
                
                if not (prev_exists and next_exists):
                    orphaned.append(task)
        
        # Calculate statistics
        total_tasks = sum(len(phase_tasks) for phase_tasks in phases.values())
        completion_rate = (valid_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        return {
            'phases': phases,
            'orphaned': orphaned,
            'stats': {
                'total_tasks': total_tasks,
                'connected_tasks': connected_tasks,
                'orphaned_tasks': len(orphaned),
                'phases_count': len(phases),
                'valid_tasks': valid_tasks,
                'completion_rate': completion_rate
            }
        }
    
    def _generate_task_node_html(self, task: Dict) -> str:
        """Generate HTML for a single task node."""
        status_class = "valid" if task['valid'] else "invalid"
        status_icon = "✅" if task['valid'] else "❌"
        
        return f"""
            <div class="task-node {status_class}">
                <div class="task-id">{status_icon} {task['task_id']}</div>
                <div class="task-title">{task['title']}</div>
                <div class="task-agent">{task['agent']}</div>
            </div>"""
    
    def wait_for_interrupt(self):
        """Keep the script running until interrupted."""
        try:
            self.console.print("\n🔄 [cyan]Analysis complete! HTML file is ready.[/cyan]")
            self.console.print("💡 [yellow]The script will keep running. Press Ctrl+C to stop and clean up.[/yellow]")
            
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.console.print("\n\n🛑 [yellow]Interrupt received. Cleaning up...[/yellow]")
            self._cleanup_temp_files()
            self.console.print("✅ [green]Cleanup completed. Goodbye![/green]")
    
    def extract_yaml_frontmatter(self, content: str) -> tuple[Optional[Dict[str, Any]], List[str]]:
        """Extract YAML front matter from markdown content."""
        errors = []
        
        # Check if content starts with YAML front matter
        if not content.strip().startswith('---'):
            return None, ["No YAML front matter found"]
        
        # Find the YAML front matter block
        yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not yaml_match:
            return None, ["Invalid YAML front matter format"]
        
        yaml_content = yaml_match.group(1)
        
        try:
            yaml_data = yaml.safe_load(yaml_content)
            return yaml_data, []
        except yaml.YAMLError as e:
            return None, [f"YAML parsing error: {str(e)}"]
    
    def extract_headers(self, content: str) -> List[str]:
        """Extract all ## headers from markdown content."""
        headers = []
        lines = content.split('\n')
        
        for line in lines:
            # Match ## headers (level 2)
            if re.match(r'^##\s+', line):
                header = line.strip().replace('##', '').strip()
                headers.append(header)
        
        return headers
    
    def validate_yaml_fields(self, yaml_data: Optional[Dict[str, Any]]) -> List[str]:
        """Validate required YAML fields."""
        if not yaml_data:
            return self.REQUIRED_YAML_FIELDS.copy()
        
        missing_fields = []
        for field in self.REQUIRED_YAML_FIELDS:
            if field not in yaml_data or yaml_data[field] is None:
                missing_fields.append(field)
        
        return missing_fields
    
    def analyze_file(self, file_path: Path) -> FileAnalysis:
        """Analyze a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return FileAnalysis(
                filename=file_path.name,
                filepath=str(file_path),
                yaml_frontmatter=None,
                headers=[],
                yaml_valid=False,
                yaml_errors=[f"Error reading file: {str(e)}"],
                missing_required_fields=self.REQUIRED_YAML_FIELDS.copy()
            )
        
        # Extract YAML front matter
        yaml_data, yaml_errors = self.extract_yaml_frontmatter(content)
        
        # Extract headers
        headers = self.extract_headers(content)
        
        # Validate YAML fields
        missing_fields = self.validate_yaml_fields(yaml_data)
        
        return FileAnalysis(
            filename=file_path.name,
            filepath=str(file_path),
            yaml_frontmatter=yaml_data,
            headers=headers,
            yaml_valid=len(yaml_errors) == 0 and len(missing_fields) == 0,
            yaml_errors=yaml_errors,
            missing_required_fields=missing_fields
        )
    
    def find_subfolders_with_md(self) -> Dict[str, int]:
        """Find subfolders that contain markdown files."""
        subfolder_counts = {}
        for subfolder in self.folder_path.iterdir():
            if subfolder.is_dir():
                md_count = len(list(subfolder.glob("*.md")))
                if md_count > 0:
                    subfolder_counts[subfolder.name] = md_count
        return subfolder_counts
    
    def analyze_folder(self) -> None:
        """Analyze all markdown files in the folder."""
        self.console.print(f"\n🔍 Analyzing folder: [bold blue]{self.folder_path}[/bold blue]")
        
        # Find all markdown files
        if self.recursive:
            md_files = list(self.folder_path.rglob("*.md"))
            self.console.print(f"Recursive search enabled")
        else:
            md_files = list(self.folder_path.glob("*.md"))
        
        if not md_files:
            self.console.print("[yellow]No markdown files found in the specified folder.[/yellow]")
            
            # Check for subfolders with markdown files
            subfolder_counts = self.find_subfolders_with_md()
            if subfolder_counts:
                self.console.print("\n📁 [cyan]Found subfolders with markdown files:[/cyan]")
                for subfolder, count in subfolder_counts.items():
                    self.console.print(f"   • [green]{subfolder}[/green]: {count} files")
                
                self.console.print(f"\n💡 [yellow]Tip:[/yellow] Use --recursive (-r) to analyze all subfolders:")
                self.console.print(f"   [dim]python {sys.argv[0]} \"{self.folder_path}\" --recursive[/dim]")
                
                self.console.print(f"\n💡 [yellow]Or analyze specific subfolders:[/yellow]")
                for subfolder in subfolder_counts.keys():
                    subfolder_path = self.folder_path / subfolder
                    self.console.print(f"   [dim]python {sys.argv[0]} \"{subfolder_path}\"[/dim]")
            
            if self.show_structure:
                self.display_folder_structure()
            return
        
        self.console.print(f"Found {len(md_files)} markdown files")
        if self.recursive:
            # Group files by their parent directory
            files_by_dir = {}
            for file_path in sorted(md_files):
                parent_dir = file_path.parent
                if parent_dir not in files_by_dir:
                    files_by_dir[parent_dir] = []
                files_by_dir[parent_dir].append(file_path)
            
            self.console.print(f"Files distributed across {len(files_by_dir)} directories")
        
        # Analyze each file
        for file_path in sorted(md_files):
            analysis = self.analyze_file(file_path)
            self.files_analysis.append(analysis)
    
    def display_folder_structure(self) -> None:
        """Display the folder structure when no markdown files are found."""
        tree = Tree(f"📁 [bold blue]{self.folder_path.name}[/bold blue] (Folder Structure)")
        
        for item in sorted(self.folder_path.iterdir()):
            if item.is_dir():
                md_count = len(list(item.glob("*.md")))
                if md_count > 0:
                    tree.add(f"📁 [green]{item.name}[/green] ({md_count} markdown files)")
                else:
                    tree.add(f"📁 [dim]{item.name}[/dim] (no markdown files)")
            else:
                tree.add(f"📄 [cyan]{item.name}[/cyan]")
        
        self.console.print(tree)
    
    def display_architecture(self) -> None:
        """Display the folder architecture analysis."""
        if not self.files_analysis:
            self.console.print("[red]No files analyzed.[/red]")
            return
        
        # Create main tree
        tree = Tree(f"📁 [bold blue]{self.folder_path.name}[/bold blue]")
        
        if self.recursive:
            # Group files by directory for recursive display
            files_by_dir = {}
            for analysis in self.files_analysis:
                file_path = Path(analysis.filepath)
                parent_dir = file_path.parent
                if parent_dir not in files_by_dir:
                    files_by_dir[parent_dir] = []
                files_by_dir[parent_dir].append(analysis)
            
            # Display each directory as a branch
            for dir_path, analyses in sorted(files_by_dir.items()):
                relative_path = dir_path.relative_to(self.folder_path)
                dir_node = tree.add(f"📁 [cyan]{relative_path}[/cyan]")
                
                for analysis in analyses:
                    self._add_file_node(dir_node, analysis)
        else:
            # Single directory display
            for analysis in self.files_analysis:
                self._add_file_node(tree, analysis)
        
        self.console.print(tree)
    
    def _add_file_node(self, parent_node, analysis: FileAnalysis):
        """Add a file node to the tree."""
        file_status = "✅" if analysis.yaml_valid else "❌"
        file_node = parent_node.add(f"{file_status} [bold]{analysis.filename}[/bold]")
        
        # YAML Front Matter section
        yaml_node = file_node.add("📋 [cyan]YAML Front Matter[/cyan]")
        
        if analysis.yaml_frontmatter:
            for key, value in analysis.yaml_frontmatter.items():
                status = "✅" if key in self.REQUIRED_YAML_FIELDS else "ℹ️"
                yaml_node.add(f"{status} [green]{key}[/green]: {value}")
        
        # Missing fields
        if analysis.missing_required_fields:
            missing_node = yaml_node.add("❌ [red]Missing Required Fields[/red]")
            for field in analysis.missing_required_fields:
                missing_node.add(f"• {field}")
        
        # YAML errors
        if analysis.yaml_errors:
            error_node = yaml_node.add("⚠️ [red]YAML Errors[/red]")
            for error in analysis.yaml_errors:
                error_node.add(f"• {error}")
        
        # Headers section
        if analysis.headers:
            headers_node = file_node.add("📝 [yellow]Headers (##)[/yellow]")
            for header in analysis.headers:
                headers_node.add(f"• {header}")
        else:
            file_node.add("📝 [dim]No ## headers found[/dim]")
    
    def display_summary_table(self) -> None:
        """Display a summary table of the analysis."""
        table = Table(title="📊 Analysis Summary")
        
        table.add_column("File", style="cyan", no_wrap=True)
        table.add_column("YAML Valid", justify="center")
        table.add_column("Headers Count", justify="center")
        table.add_column("Missing Fields", justify="center")
        table.add_column("Status", justify="center")
        
        for analysis in self.files_analysis:
            yaml_status = "✅" if analysis.yaml_valid else "❌"
            headers_count = str(len(analysis.headers))
            missing_count = str(len(analysis.missing_required_fields))
            overall_status = "✅ Valid" if analysis.yaml_valid else "❌ Issues"
            
            table.add_row(
                analysis.filename,
                yaml_status,
                headers_count,
                missing_count,
                overall_status
            )
        
        self.console.print(table)
    
    def display_validation_details(self) -> None:
        """Display detailed validation information."""
        self.console.print("\n📋 [bold]YAML Front Matter Validation Details[/bold]")
        
        for analysis in self.files_analysis:
            # Create panel for each file
            if not analysis.yaml_valid:
                content = []
                
                if analysis.yaml_errors:
                    content.append("[red]YAML Errors:[/red]")
                    for error in analysis.yaml_errors:
                        content.append(f"  • {error}")
                
                if analysis.missing_required_fields:
                    content.append("\n[red]Missing Required Fields:[/red]")
                    for field in analysis.missing_required_fields:
                        content.append(f"  • {field}")
                
                if content:
                    panel = Panel(
                        "\n".join(content),
                        title=f"❌ {analysis.filename}",
                        border_style="red"
                    )
                    self.console.print(panel)
    
    def get_export_data(self) -> Dict[str, Any]:
        """Prepare data for export."""
        return {
            "analysis_metadata": {
                "timestamp": self.analysis_timestamp.isoformat(),
                "folder_path": str(self.folder_path),
                "recursive": self.recursive,
                "total_files": len(self.files_analysis),
                "valid_files": sum(1 for analysis in self.files_analysis if analysis.yaml_valid),
                "invalid_files": sum(1 for analysis in self.files_analysis if not analysis.yaml_valid)
            },
            "files": [asdict(analysis) for analysis in self.files_analysis],
            "summary": {
                "required_yaml_fields": self.REQUIRED_YAML_FIELDS,
                "total_headers": sum(len(analysis.headers) for analysis in self.files_analysis),
                "files_with_errors": [analysis.filename for analysis in self.files_analysis if analysis.yaml_errors],
                "files_missing_fields": [analysis.filename for analysis in self.files_analysis if analysis.missing_required_fields]
            }
        }
    
    def export_to_json(self) -> str:
        """Export analysis results to JSON format."""
        data = self.get_export_data()
        timestamp = self.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        filename = f"architecture_analysis_{timestamp}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return str(filepath)
    
    def export_to_csv(self) -> str:
        """Export analysis results to CSV format."""
        timestamp = self.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        filename = f"architecture_analysis_{timestamp}.csv"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write headers
            writer.writerow([
                'Filename', 'Filepath', 'YAML_Valid', 'Headers_Count', 
                'Missing_Fields_Count', 'YAML_Errors_Count', 'Headers', 
                'Missing_Fields', 'YAML_Errors'
            ])
            
            # Write data
            for analysis in self.files_analysis:
                writer.writerow([
                    analysis.filename,
                    analysis.filepath,
                    analysis.yaml_valid,
                    len(analysis.headers),
                    len(analysis.missing_required_fields),
                    len(analysis.yaml_errors),
                    '; '.join(analysis.headers),
                    '; '.join(analysis.missing_required_fields),
                    '; '.join(analysis.yaml_errors)
                ])
        
        return str(filepath)
    
    def export_to_html(self) -> str:
        """Export analysis results to HTML format."""
        timestamp = self.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        filename = f"architecture_analysis_{timestamp}.html"
        filepath = self.output_dir / filename
        
        data = self.get_export_data()
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Analysis Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1, h2, h3 {{ color: #333; }}
        .metadata {{ background: #e8f4fd; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .summary {{ background: #f0f8f0; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; font-weight: bold; }}
        .valid {{ color: #28a745; }}
        .invalid {{ color: #dc3545; }}
        .file-details {{ margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
        .headers {{ background: #fff3cd; padding: 10px; border-radius: 3px; }}
        .errors {{ background: #f8d7da; padding: 10px; border-radius: 3px; }}
        .missing {{ background: #f8d7da; padding: 10px; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Architecture Analysis Report</h1>
        
        <div class="metadata">
            <h2>📋 Analysis Metadata</h2>
            <p><strong>Timestamp:</strong> {data['analysis_metadata']['timestamp']}</p>
            <p><strong>Folder Path:</strong> {data['analysis_metadata']['folder_path']}</p>
            <p><strong>Recursive Analysis:</strong> {data['analysis_metadata']['recursive']}</p>
            <p><strong>Total Files:</strong> {data['analysis_metadata']['total_files']}</p>
        </div>
        
        <div class="summary">
            <h2>📈 Summary</h2>
            <p><strong>Valid Files:</strong> <span class="valid">{data['analysis_metadata']['valid_files']}</span></p>
            <p><strong>Invalid Files:</strong> <span class="invalid">{data['analysis_metadata']['invalid_files']}</span></p>
            <p><strong>Success Rate:</strong> {(data['analysis_metadata']['valid_files']/data['analysis_metadata']['total_files']*100):.1f}%</p>
            <p><strong>Total Headers:</strong> {data['summary']['total_headers']}</p>
        </div>
        
        <h2>📁 Files Analysis</h2>
        <table>
            <thead>
                <tr>
                    <th>File</th>
                    <th>Status</th>
                    <th>Headers</th>
                    <th>Missing Fields</th>
                    <th>Errors</th>
                </tr>
            </thead>
            <tbody>"""
        
        for analysis in self.files_analysis:
            status_class = "valid" if analysis.yaml_valid else "invalid"
            status_text = "✅ Valid" if analysis.yaml_valid else "❌ Invalid"
            
            html_content += f"""
                <tr>
                    <td>{analysis.filename}</td>
                    <td class="{status_class}">{status_text}</td>
                    <td>{len(analysis.headers)}</td>
                    <td>{len(analysis.missing_required_fields)}</td>
                    <td>{len(analysis.yaml_errors)}</td>
                </tr>"""
        
        html_content += """
            </tbody>
        </table>
        
        <h2>📝 Detailed File Analysis</h2>"""
        
        for analysis in self.files_analysis:
            html_content += f"""
        <div class="file-details">
            <h3>📄 {analysis.filename}</h3>
            <p><strong>Path:</strong> {analysis.filepath}</p>
            <p><strong>YAML Valid:</strong> <span class="{'valid' if analysis.yaml_valid else 'invalid'}">{'✅ Yes' if analysis.yaml_valid else '❌ No'}</span></p>"""
            
            if analysis.headers:
                html_content += f"""
            <div class="headers">
                <h4>📝 Headers ({len(analysis.headers)})</h4>
                <ul>{''.join(f'<li>{header}</li>' for header in analysis.headers)}</ul>
            </div>"""
            else:
                html_content += "<p>No headers found</p>"
            
            if analysis.missing_required_fields:
                html_content += f"""
            <div class="missing">
                <h4>❌ Missing Required Fields ({len(analysis.missing_required_fields)})</h4>
                <ul>{''.join(f'<li>{field}</li>' for field in analysis.missing_required_fields)}</ul>
            </div>"""
            
            if analysis.yaml_errors:
                html_content += f"""
            <div class="errors">
                <h4>⚠️ YAML Errors ({len(analysis.yaml_errors)})</h4>
                <ul>{''.join(f'<li>{error}</li>' for error in analysis.yaml_errors)}</ul>
            </div>"""
            
            html_content += "</div>"
        
        html_content += """
    </div>
</body>
</html>"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(filepath)
    
    def export_results(self) -> List[str]:
        """Export results in the specified format(s)."""
        exported_files = []
        
        if self.export_format == "all":
            formats = ["json", "csv", "html"]
        else:
            formats = [self.export_format]
        
        for fmt in formats:
            try:
                if fmt == "json":
                    filepath = self.export_to_json()
                elif fmt == "csv":
                    filepath = self.export_to_csv()
                elif fmt == "html":
                    filepath = self.export_to_html()
                
                exported_files.append(filepath)
                self.console.print(f"✅ Exported {fmt.upper()}: [green]{filepath}[/green]")
            
            except Exception as e:
                self.console.print(f"❌ Failed to export {fmt.upper()}: [red]{e}[/red]")
        
        return exported_files

    def run_analysis(self) -> None:
        """Run the complete analysis and display results."""
        self.analyze_folder()
        
        if not self.files_analysis:
            return
        
        # Display results
        self.display_architecture()
        self.console.print("\n")
        self.display_summary_table()
        self.display_validation_details()
        
        # Final summary
        valid_files = sum(1 for analysis in self.files_analysis if analysis.yaml_valid)
        total_files = len(self.files_analysis)
        
        self.console.print(f"\n🎯 [bold]Final Summary:[/bold]")
        self.console.print(f"   Valid files: {valid_files}/{total_files}")
        self.console.print(f"   Success rate: {(valid_files/total_files)*100:.1f}%")
        
        # Export if requested
        if self.export_format:
            self.console.print(f"\\n📤 [bold]Exporting Results...[/bold]")
            exported_files = self.export_results()
            if exported_files:
                self.console.print(f"\\n✅ [green]Export completed! Files saved to: {self.output_dir}[/green]")
        
        # Handle interactive HTML export
        if self.export_html:
            self.console.print(f"\\n🌐 [bold]Creating Interactive HTML Report...[/bold]")
            try:
                html_file = self.export_html_interactive()
                html_filename = os.path.basename(html_file)
                file_url = f"file://{os.path.abspath(html_file)}"
                
                self.console.print(f"\\n✅ [green]HTML report created![/green]")
                self.console.print(f"📁 [yellow]File:[/yellow] [bold]{html_filename}[/bold]")
                self.console.print(f"📂 [yellow]Location:[/yellow] {os.path.dirname(html_file)}")
                
                self.console.print(f"\\n🌐 [cyan]Open the HTML file:[/cyan]")
                self.console.print(f"   [dim]• Double-click the file: {html_filename}[/dim]")
                self.console.print(f"   [dim]• Or run: xdg-open {html_filename}[/dim]")
                self.console.print(f"   [dim]• Or run: firefox {html_filename}[/dim]")
                self.console.print(f"   [dim]• Direct URL: {file_url}[/dim]")
                
                # Try to open automatically
                try:
                    import subprocess
                    # Try to open with default browser
                    subprocess.run(['xdg-open', html_file], check=False, capture_output=True)
                    self.console.print(f"\\n🚀 [green]Attempting to open in default browser...[/green]")
                except:
                    pass
                
                # Wait for interrupt
                self.wait_for_interrupt()
                
            except Exception as e:
                self.console.print(f"❌ [red]Failed to create interactive HTML: {e}[/red]")

def main():
    """Main function to run the architecture analyzer."""
    parser = argparse.ArgumentParser(
        description="Analyze folder architecture and validate YAML front matter in markdown files"
    )
    parser.add_argument(
        "folder_path",
        help="Path to the folder to analyze"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Recursively analyze all subfolders"
    )
    parser.add_argument(
        "--show-structure", "-s",
        action="store_true",
        help="Show folder structure even when no markdown files found"
    )
    parser.add_argument(
        "--export", "-e",
        choices=["json", "csv", "html", "all"],
        help="Export analysis results to specified format(s)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="./exports",
        help="Output directory for exported files (default: ./exports)"
    )
    parser.add_argument(
        "--export-html",
        action="store_true",
        help="Export to HTML and open in browser, keep running until Ctrl+C (auto-cleanup)"
    )
    
    args = parser.parse_args()
    
    try:
        analyzer = ArchitectureAnalyzer(args.folder_path, args.recursive, args.show_structure, args.export, args.output_dir, args.export_html)
        analyzer.run_analysis()
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 