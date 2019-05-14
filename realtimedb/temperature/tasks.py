from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta
from .models import Temperature
from random import uniform

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(timedelta(seconds=10)),
    name='update-temperature',
    ignore_result=True
)
def update_temperature():
    """
    Update temperature in db by using randomized values
    :return: void
    """
    updated = []
    for temperature in Temperature.objects.all():
        diff = uniform(-1, 1)
        temperature.value = round(temperature.value + diff, 2)
        temperature.save()
        updated.append(temperature)

    logger.info(f"Updated temperature: {updated}")
