#!/usr/bin/env python3

import unittest
from test.generic.optim_test_util import TestOptimizer

from classy_vision.optim.sgd import SGD


class TestSGDOptimizer(TestOptimizer, unittest.TestCase):
    def _get_config(self):
        return {
            "name": "sgd",
            "num_epochs": 90,
            "lr": 0.1,
            "momentum": 0.9,
            "weight_decay": 0.0001,
            "nesterov": False,
        }

    def _instance_to_test(self):
        return SGD
