"""End-to-end analysis of ventilator sensor data."""
from ventplotting.files import signals
from ventplotting.utilities import paths


ANALYSIS_STAGES = [
    'raw_all_signals', 'raw_signals'
]


def analysis_stage_before(stage, comparison_stage):
    """Check whether the given analysis stage is before or at the comparison stage."""
    stage_index = ANALYSIS_STAGES.index(stage)
    comparison_index = ANALYSIS_STAGES.index(comparison_stage)
    return stage_index <= comparison_index


class VentAnalyzer(object):
    """Ventilator signal analyzer."""

    def __init__(self, vent_analyzer=None, link_endpoint='raw_signals'):
        """Initialize analyzer object without any data or configs loaded.

        If vent_analyzer is given, members (representing analysis stages) will
        be linked to it instead of respective new objects being instantiated.
        All members will be linked up to and including the member specified by
        the link_endpoint parameter.
        """
        def link(reference_stage):
            return (
                vent_analyzer is not None
                and analysis_stage_before(reference_stage, link_endpoint)
            )

        if link('raw_signals'):
            self.raw_signals = vent_analyzer.raw_signals
        else:
            self._make_empty_raw_signals()

    def _make_empty_raw_signals(self):
        self.raw_signals = signals.RawSignalSet()

    # DATA

    def load_data(self, name, dir):
        """Load all data files needed for analysis."""
        self.raw_signals.load_csv(paths.csv_name_to_path(name, dir=dir))

    # CONFIGS

    def load_configs(self, name, dir):
        """Load all configuration files with a shared name and directory."""
        pass
