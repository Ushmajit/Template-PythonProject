#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")


name = "Template-PythonProject"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("mockito")
    project.set_property("coverage_threshold_warn", 90)
    project.set_property("coverage_branch_threshold_warn", 80)
    project.set_property("coverage_branch_partial_threshold_warn", 80)