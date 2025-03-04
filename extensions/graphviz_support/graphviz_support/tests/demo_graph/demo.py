#!/usr/bin/env python3
# Copyright 2004-present Facebook. All Rights Reserve

import labgraph as lg
from typing import Tuple
from .noise_generator import NoiseGeneratorConfig, NoiseGenerator
from .rolling_averager import RollingConfig, RollingAverager
from .amplifier import AmplifierConfig, Amplifier
from .attenuator import AttenuatorConfig, Attenuator
from .sink import Sink


SAMPLE_RATE = 10.0
NUM_FEATURES = 100
WINDOW = 2.0
REFRESH_RATE = 2.0
OUT_IN_RATIO = 1.2
ATTENUATION = 5.0


class Demo(lg.Graph):
    NOISE_GENERATOR: NoiseGenerator
    ROLLING_AVERAGER: RollingAverager
    AMPLIFIER: Amplifier
    ATTENUATOR: Attenuator
    SINK: Sink

    def setup(self) -> None:
        self.NOISE_GENERATOR.configure(
            NoiseGeneratorConfig(
                sample_rate=SAMPLE_RATE,
                num_features=NUM_FEATURES
            )
        )

        self.ROLLING_AVERAGER.configure(
            RollingConfig(window=WINDOW)
        )

        self.AMPLIFIER.configure(
            AmplifierConfig(out_in_ratio=OUT_IN_RATIO)
        )

        self.ATTENUATOR.configure(
            AttenuatorConfig(attenuation=ATTENUATION)
        )

    def connections(self) -> lg.Connections:
        return (
            (self.NOISE_GENERATOR.OUTPUT, self.ROLLING_AVERAGER.INPUT),
            (self.NOISE_GENERATOR.OUTPUT, self.AMPLIFIER.INPUT),
            (self.NOISE_GENERATOR.OUTPUT, self.ATTENUATOR.INPUT),
            (self.ROLLING_AVERAGER.OUTPUT, self.SINK.INPUT_1),
            (self.AMPLIFIER.OUTPUT, self.SINK.INPUT_2),
            (self.ATTENUATOR.OUTPUT, self.SINK.INPUT_3),
        )

    def process_modules(self) -> Tuple[lg.Module, ...]:
        return (
            self.NOISE_GENERATOR,
            self.ROLLING_AVERAGER,
            self.AMPLIFIER,
            self.ATTENUATOR,
            self.SINK
        )
