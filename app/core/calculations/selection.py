# Copyright (c) 2016-2022 Association of Universities for Research in Astronomy, Inc. (AURA)
# For license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause

from dataclasses import dataclass
from typing import Mapping, NoReturn

from lucupy.minimodel import Group, ProgramID, Site

from .nightevents import NightEvents
from .programinfo import ProgramInfo


@dataclass(frozen=True)
class Selection:
    """
    The selection of information passed by the Selector to the Optimizer.
    This includes the list of programs that are schedulable and the night event for the nights under consideration.
    """
    program_info: Mapping[ProgramID, ProgramInfo]
    night_events: Mapping[Site, NightEvents]

    def show(self) -> NoReturn:
        for prog_info in self.program_info.values():
            prog_info.program.show()

    def show_groups(self) -> NoReturn:
        for prog_info in self.program_info.values():
            print(f'*** PROGRAM {prog_info.program.id}')
            for group_info in prog_info.group_data.values():
                print(f'    {group_info.group.unique_id()}')

    def __post_init__(self):
        object.__setattr__(self, 'program_ids', frozenset(self.program_info.keys()))
