import random
import time

from hyrex import HyrexRegistry

hy = HyrexRegistry()


@hy.task
def test_task():
    """A simple test task that sleeps for a random duration."""
    sleep_duration = random.uniform(0, 2)
    time.sleep(sleep_duration)


@hy.task
def send_n_test_tasks(n: int):
    """Enqueue n test_task instances."""
    for i in range(n):
        test_task.send()
    return f"Enqueued {n} test tasks"


# Simple ETL Workflow Example
@hy.task
def extract_data():
    """Extract data from source."""
    print("📊 Extracting data from source...")
    time.sleep(1)
    print("✓ Extract complete")


@hy.task
def transform_data():
    """Transform the extracted data."""
    print("🔄 Transforming data...")
    time.sleep(1)
    print("✓ Transform complete")


@hy.task
def load_data():
    """Load data to destination."""
    print("💾 Loading data to destination...")
    time.sleep(1)
    print("✓ Load complete")


@hy.workflow(queue="etl")
def simple_etl_workflow():
    """A simple ETL workflow that chains extract, transform, and load tasks."""
    extract_data >> transform_data >> load_data
