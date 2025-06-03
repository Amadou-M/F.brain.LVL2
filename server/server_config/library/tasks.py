from celery import shared_task

@shared_task
def scrape_data():
    # Exemple de tâche de scraping
    print("Scraping data...")
    return "Done"