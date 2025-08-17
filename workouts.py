#!/usr/bin/env python3
"""
WORKOUTS CLI - Vintage Terminal Workout Data Analyzer
═══════════════════════════════════════════════════════
A retro-styled command line tool for analyzing workout data
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from datetime import datetime

# Initialize rich console for styling
console = Console()


def display_banner():
    """Display retro terminal banner with clear workout theme"""
    banner = Text.assemble(
        ("    ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗███████╗\n", "cyan"),
        ("    ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝\n", "cyan"),
        ("    ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║   ██║██║   ██║   ██║   ███████╗\n", "cyan"),
        ("    ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║   ██║██║   ██║   ██║   ╚════██║\n", "green"),
        ("    ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗╚██████╔╝╚██████╔╝   ██║   ███████║\n", "green"),
        ("     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝\n", "green"),
        ("\n", "white"),
        ("                            🏋️‍♂️ CLASSIFIED DATA TERMINAL 🏋️‍♀️\n", "bold bright_white"),
        ("                              💪 STRENGTH ANALYSIS SYSTEM 💪\n", "bold bright_green"),
    )

    subtitle = Text("🔒 SECURE WORKOUT INTELLIGENCE v2.0 🔒", style="bold yellow")
    timestamp = Text(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SECURE CONNECTION ESTABLISHED",
                     style="dim green")

    console.print()
    console.print(
        Panel(banner, subtitle=subtitle, style="bright_white on black", title="[bold red]⚡ MISSION CONTROL ⚡[/]"))
    console.print(timestamp)
    console.print()


def load_workout_data(file_path):
    """Load and validate workout CSV data"""
    try:
        console.print(f"[bold green]▶[/] Loading classified workout data from: {file_path}")

        # Read CSV with pandas
        df = pd.read_csv(file_path)

        # Basic validation
        required_columns = ['Date', 'Exercise', 'Sets', 'Reps per Set', 'Weight Used (lbs)', 'Total Volume (lbs)']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            console.print(f"[bold red]✗[/] CRITICAL ERROR: Missing columns: {missing_columns}")
            return None

        # Convert Date column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        console.print(f"[bold green]✓[/] Data loaded successfully. Records found: {len(df)}")
        console.print(
            f"[bold green]✓[/] Date range: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")

        return df

    except FileNotFoundError:
        console.print(f"[bold red]✗[/] CLASSIFIED FILE NOT FOUND: {file_path}")
        return None
    except Exception as e:
        console.print(f"[bold red]✗[/] DATA CORRUPTION DETECTED: {str(e)}")
        return None


def create_volume_chart(df):
    """Create ASCII bar chart of total volume by date"""
    console.print("\n[bold cyan]═══ VOLUME ANALYSIS ═══[/]")

    # Group by date and sum total volume
    daily_volume = df.groupby('Date')['Total Volume (lbs)'].sum().sort_index()

    # Create ASCII bar chart
    max_volume = daily_volume.max()
    max_width = 50  # Maximum bar width in characters

    console.print(f"\n[bold yellow]Total Volume by Date (Max: {max_volume:,.0f} lbs)[/]\n")

    for date, volume in daily_volume.items():
        bar_length = int((volume / max_volume) * max_width)
        bar = "█" * bar_length
        percentage = (volume / max_volume) * 100

        date_str = date.strftime('%m-%d')
        console.print(f"{date_str} │{bar:<50}│ {volume:>6,.0f} lbs ({percentage:>5.1f}%)")

    console.print(f"\n[dim]{'─' * 70}[/]")
    console.print(f"[bold green]TOTAL CLASSIFIED VOLUME: {daily_volume.sum():,.0f} lbs[/]")


def display_quick_stats(df):
    """Display quick workout statistics"""
    total_workouts = df['Date'].nunique()
    total_exercises = df['Exercise'].nunique()
    total_volume = df['Total Volume (lbs)'].sum()
    avg_volume_per_workout = total_volume / total_workouts

    stats_table = Table(title="[bold red]CLASSIFIED WORKOUT INTELLIGENCE[/]", style="bright_white on black")
    stats_table.add_column("Metric", style="cyan", no_wrap=True)
    stats_table.add_column("Value", style="bright_green", justify="right")

    stats_table.add_row("Total Workouts", f"{total_workouts}")
    stats_table.add_row("Unique Exercises", f"{total_exercises}")
    stats_table.add_row("Total Volume", f"{total_volume:,.0f} lbs")
    stats_table.add_row("Avg Volume/Workout", f"{avg_volume_per_workout:,.0f} lbs")

    console.print(stats_table)


def interactive_session(df):
    """Interactive session for exploring workout data"""
    console.print("\n[bold cyan]═══ ENTERING INTERACTIVE MODE ═══[/]")
    console.print("[dim]Available commands: 'chart', 'stats', 'exercises', 'help', 'exit'[/]")

    while True:
        try:
            command = console.input("\n[bold green]CLASSIFIED > [/]").strip().lower()

            if command in ['exit', 'quit', 'q']:
                console.print("[bold red]MISSION TERMINATED[/]")
                console.print("[dim]Secure connection closed. Data wiped from memory.[/]")
                break

            elif command == 'help':
                console.print("\n[bold yellow]AVAILABLE COMMANDS:[/]")
                console.print("  [cyan]chart[/]  - Display volume chart")
                console.print("  [cyan]stats[/]  - Show workout statistics")
                console.print("  [cyan]exercises[/] - List all exercises")
                console.print("  [cyan]help[/]   - Show this help")
                console.print("  [cyan]exit[/]   - Terminate session")

            elif command == 'chart':
                create_volume_chart(df)

            elif command == 'stats':
                display_quick_stats(df)

            elif command == 'exercises':
                exercise_list = df['Exercise'].unique()
                console.print(f"\n[bold cyan]CLASSIFIED EXERCISE DATABASE ({len(exercise_list)} entries):[/]")
                for i, exercise in enumerate(exercise_list, 1):
                    total_sets = df[df['Exercise'] == exercise]['Sets'].sum()
                    console.print(f"  {i:2d}. {exercise} [dim]({total_sets} total sets)[/]")

            elif command == '':
                continue

            else:
                console.print(f"[bold red]UNKNOWN COMMAND:[/] '{command}'")
                console.print("[dim]Type 'help' for available commands[/]")

        except KeyboardInterrupt:
            console.print("\n[bold red]EMERGENCY SHUTDOWN INITIATED[/]")
            break
        except EOFError:
            console.print("\n[bold red]CONNECTION LOST[/]")
            break


def main():
    parser = argparse.ArgumentParser(
        description="CLASSIFIED: Workout Data Analysis Terminal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  workouts --file data.csv
  workouts -f workout_data.csv --stats
  workouts -f data.csv --interactive
        """
    )

    parser.add_argument(
        '--file', '-f',
        required=True,
        help='Path to workout CSV file'
    )

    parser.add_argument(
        '--stats', '-s',
        action='store_true',
        help='Display detailed statistics'
    )

    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Enter interactive exploration mode'
    )

    args = parser.parse_args()

    # Display banner
    display_banner()

    # Load data
    df = load_workout_data(args.file)
    if df is None:
        console.print("[bold red]MISSION ABORTED: Cannot proceed without valid data[/]")
        sys.exit(1)

    # Display stats if requested
    if args.stats:
        display_quick_stats(df)
        console.print()

    # Create volume chart
    create_volume_chart(df)

    # Enter interactive mode if requested or by default
    if args.interactive:
        interactive_session(df)
    else:
        # Auto-enter interactive mode by default
        console.print(f"\n[dim green]{'═' * 70}[/]")
        console.print("[bold green]DATA ANALYSIS COMPLETE[/]")
        console.print("[dim]Entering interactive mode... (type 'exit' to quit)[/]")
        interactive_session(df)

    console.print(f"\n[dim green]{'═' * 70}[/]")
    console.print("[bold green]MISSION COMPLETE: All systems offline[/]")


if __name__ == "__main__":
    main()
