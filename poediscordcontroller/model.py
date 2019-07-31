from dataclasses import dataclass
from typing import Optional, Callable, Union
from enum import Enum

@dataclass
class Initiator:
    pass

@dataclass
class Data:
    pass

class JobResult(Enum):
    Complete = 0
    Delayed = 1
    Failed = 2

@dataclass
class JobId:
    queue: str
    job_id: int

    @property
    def fqn(self):
        return f"job: {self.queue}-{self.job_id}"

@dataclass
class Job:
    job_id: JobId
    initiator: Initiator
    data: Data
    stage: Union[Callable, JobResult, None] = None
