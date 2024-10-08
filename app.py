
# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# isort: skip_file

"""Streamlit.

How to use Streamlit in 3 seconds:

    1. Write an app
    >>> import streamlit as st
    >>> st.write(anything_you_want)

    2. Run your app
    $ streamlit run my_script.py

    3. Use your app
    A new tab will open on your browser. That's your Streamlit app!

    4. Modify your code, save it, and watch changes live on your browser.

Take a look at the other commands in this module to find out what else
Streamlit can do:

    >>> dir(streamlit)

Or try running our "Hello World":

    $ streamlit hello

For more detailed info, see https://docs.streamlit.io.
"""

# IMPORTANT: Prefix with an underscore anything that the user shouldn't see.

import os as _os

# Set Matplotlib backend to avoid a crash.
# The default Matplotlib backend crashes Python on OSX when run on a thread
# that's not the main thread, so here we set a safer backend as a fix.
# This fix is OS-independent. We didn't see a good reason to make this
# Mac-only. Consistency within Streamlit seemed more important.
# IMPORTANT: This needs to run on top of all imports before any other
# import of matplotlib could happen.
_os.environ["MPLBACKEND"] = "Agg"


# Must be at the top, to avoid circular dependency.
from streamlit import logger as _logger
from streamlit import config as _config
from streamlit.deprecation_util import deprecate_func_name as _deprecate_func_name
from streamlit.version import STREAMLIT_VERSION_STRING as _STREAMLIT_VERSION_STRING

# Give the package a version.
__version__ = _STREAMLIT_VERSION_STRING

# DeltaGenerator methods:
# We initialize them here so that it is clear where they are instantiated.
# Further, it helps us to break circular imports because the DeltaGenerator
# imports the different elements but some elements also require DeltaGenerator
# functions such as the dg_stack. Now, elements that require DeltaGenerator functions
# can import the singleton module.
from streamlit.delta_generator_singletons import (
    DeltaGeneratorSingleton as _DeltaGeneratorSingleton,
)
from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
from streamlit.elements.lib.mutable_status_container import (
    StatusContainer as _StatusContainer,
)
from streamlit.elements.lib.dialog import Dialog as _Dialog

# instantiate the DeltaGeneratorSingleton
_dg_singleton = _DeltaGeneratorSingleton(
    delta_generator_cls=_DeltaGenerator,
    status_container_cls=_StatusContainer,
    dialog_container_cls=_Dialog,
)
_main = _dg_singleton._main_dg
sidebar = _dg_singleton._sidebar_dg
_event = _dg_singleton._event_dg
_bottom = _dg_singleton._bottom_dg


from streamlit.elements.dialog_decorator import (
    dialog_decorator as _dialog_decorator,
    experimental_dialog_decorator as _experimental_dialog_decorator,
)
from streamlit.runtime.caching import (
    cache_resource as _cache_resource,
    cache_data as _cache_data,
    cache as _cache,
)
from streamlit.runtime.connection_factory import (
    connection_factory as _connection,
)
from streamlit.runtime.fragment import (
    experimental_fragment as _experimental_fragment,
    fragment as _fragment,
)
from streamlit.runtime.metrics_util import gather_metrics as _gather_metrics
from streamlit.runtime.secrets import secrets_singleton as _secrets_singleton
from streamlit.runtime.context import ContextProxy as _ContextProxy
from streamlit.runtime.state import (
    SessionStateProxy as _SessionStateProxy,
    QueryParamsProxy as _QueryParamsProxy,
)
from streamlit.user_info import UserInfoProxy as _UserInfoProxy
from streamlit.commands.experimental_query_params import (
    get_query_params as _get_query_params,
    set_query_params as _set_query_params,
)

import streamlit.column_config as _column_config

# Modules that the user should have access to. These are imported with the "as" syntax
# and the same name; note that renaming the import with "as" does not make it an
# explicit export. In this case, you should import it with an underscore to make clear
# that it is internal and then assign it to a variable with the new intended name.
# You can check the export behavior by running 'mypy --strict example_app.py', which
# disables implicit_reexport, where you use the respective command in the example_app.py
# Streamlit app.

from streamlit.commands.echo import echo as echo
from streamlit.commands.logo import logo as logo
from streamlit.commands.navigation import navigation as navigation
from streamlit.navigation.page import Page as Page
from streamlit.elements.spinner import spinner as spinner

from streamlit.commands.page_config import set_page_config as set_page_config
from streamlit.commands.execution_control import (
    stop as stop,
    rerun as rerun,
    switch_page as switch_page,
)


def _update_logger() -> None:
    _logger.set_log_level(_config.get_option("logger.level").upper())
    _logger.update_formatter()
    _logger.init_tornado_logs()


# Make this file only depend on config option in an asynchronous manner. This
# avoids a race condition when another file (such as a test file) tries to pass
# in an alternative config.
_config.on_config_parsed(_update_logger, True)

secrets = _secrets_singleton

altair_chart = _main.altair_chart
area_chart = _main.area_chart
audio = _main.audio
balloons = _main.balloons
bar_chart = _main.bar_chart
bokeh_chart = _main.bokeh_chart
button = _main.button
caption = _main.caption
camera_input = _main.camera_input
chat_message = _main.chat_message
chat_input = _main.chat_input
checkbox = _main.checkbox
code = _main.code
columns = _main.columns
tabs = _main.tabs
container = _main.container
dataframe = _main.dataframe
data_editor = _main.data_editor
date_input = _main.date_input
divider = _main.divider
download_button = _main.download_button
expander = _main.expander
feedback = _main.feedback
pydeck_chart = _main.pydeck_chart
empty = _main.empty
error = _main.error
exception = _main.exception
file_uploader = _main.file_uploader
form = _main.form
form_submit_button = _main.form_submit_button
graphviz_chart = _main.graphviz_chart
header = _main.header
help = _main.help
html = _main.html
image = _main.image
info = _main.info
json = _main.json
latex = _main.latex
line_chart = _main.line_chart
link_button = _main.link_button
map = _main.map
markdown = _main.markdown
metric = _main.metric
multiselect = _main.multiselect
number_input = _main.number_input
page_link = _main.page_link
plotly_chart = _main.plotly_chart
popover = _main.popover
progress = _main.progress
pyplot = _main.pyplot
radio = _main.radio
scatter_chart = _main.scatter_chart
selectbox = _main.selectbox
select_slider = _main.select_slider
slider = _main.slider
snow = _main.snow
subheader = _main.subheader
success = _main.success
table = _main.table
text = _main.text
text_area = _main.text_area
text_input = _main.text_input
toggle = _main.toggle
time_input = _main.time_input
title = _main.title
vega_lite_chart = _main.vega_lite_chart
video = _main.video
warning = _main.warning
write = _main.write
write_stream = _main.write_stream
color_picker = _main.color_picker
status = _main.status

# Events - Note: these methods cannot be called directly on sidebar
# (ex: st.sidebar.toast)
toast = _event.toast

# Config
# We add the metrics tracking here, since importing
# gather_metrics in config causes a circular dependency
get_option = _gather_metrics("get_option", _config.get_option)
set_option = _gather_metrics("set_option", _config.set_user_option)

# Session State
session_state = _SessionStateProxy()

query_params = _QueryParamsProxy()

context = _ContextProxy()

# Caching
cache_data = _cache_data
cache_resource = _cache_resource
# `st.cache` is deprecated and should be removed soon
cache = _cache

# Namespaces
column_config = _column_config

# Connection
connection = _connection

# Fragment and dialog
dialog = _dialog_decorator
fragment = _fragment

# Experimental APIs
experimental_audio_input = _main.experimental_audio_input
experimental_dialog = _experimental_dialog_decorator
experimental_fragment = _experimental_fragment
experimental_user = _UserInfoProxy()

_EXPERIMENTAL_QUERY_PARAMS_DEPRECATE_MSG = "Refer to our [docs page](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params) for more information."

experimental_get_query_params = _deprecate_func_name(
    _get_query_params,
    "experimental_get_query_params",
    "2024-04-11",
    _EXPERIMENTAL_QUERY_PARAMS_DEPRECATE_MSG,
    name_override="query_params",
)
experimental_set_query_params = _deprecate_func_name(
    _set_query_params,
    "experimental_set_query_params",
    "2024-04-11",
    _EXPERIMENTAL_QUERY_PARAMS_DEPRECATE_MSG,
    name_override="query_params",
)


# make it possible to call streamlit.components.v1.html etc. by importing it here
# import in the very end to avoid partially-initialized module import errors, because
# streamlit.components.v1 also uses some streamlit imports
import streamlit.components.v1  # noqa: F401



from __future__ import annotations


# start delvewheel patch
def _delvewheel_patch_1_8_2():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pandas.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_8_2()
del _delvewheel_patch_1_8_2
# end delvewheel patch

import os
import warnings

__docformat__ = "restructuredtext"

# Let users know if they're missing any of our hard dependencies
_hard_dependencies = ("numpy", "pytz", "dateutil")
_missing_dependencies = []

for _dependency in _hard_dependencies:
    try:
        __import__(_dependency)
    except ImportError as _e:  # pragma: no cover
        _missing_dependencies.append(f"{_dependency}: {_e}")

if _missing_dependencies:  # pragma: no cover
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(_missing_dependencies)
    )
del _hard_dependencies, _dependency, _missing_dependencies

try:
    # numpy compat
    from pandas.compat import (
        is_numpy_dev as _is_numpy_dev,  # pyright: ignore[reportUnusedImport] # noqa: F401
    )
except ImportError as _err:  # pragma: no cover
    _module = _err.name
    raise ImportError(
        f"C extension: {_module} not built. If you want to import "
        "pandas from the source directory, you may need to run "
        "'python setup.py build_ext' to build the C extensions first."
    ) from _err

from pandas._config import (
    get_option,
    set_option,
    reset_option,
    describe_option,
    option_context,
    options,
)

# let init-time option registration happen
import pandas.core.config_init  # pyright: ignore[reportUnusedImport] # noqa: F401

from pandas.core.api import (
    # dtype
    ArrowDtype,
    Int8Dtype,
    Int16Dtype,
    Int32Dtype,
    Int64Dtype,
    UInt8Dtype,
    UInt16Dtype,
    UInt32Dtype,
    UInt64Dtype,
    Float32Dtype,
    Float64Dtype,
    CategoricalDtype,
    PeriodDtype,
    IntervalDtype,
    DatetimeTZDtype,
    StringDtype,
    BooleanDtype,
    # missing
    NA,
    isna,
    isnull,
    notna,
    notnull,
    # indexes
    Index,
    CategoricalIndex,
    RangeIndex,
    MultiIndex,
    IntervalIndex,
    TimedeltaIndex,
    DatetimeIndex,
    PeriodIndex,
    IndexSlice,
    # tseries
    NaT,
    Period,
    period_range,
    Timedelta,
    timedelta_range,
    Timestamp,
    date_range,
    bdate_range,
    Interval,
    interval_range,
    DateOffset,
    # conversion
    to_numeric,
    to_datetime,
    to_timedelta,
    # misc
    Flags,
    Grouper,
    factorize,
    unique,
    value_counts,
    NamedAgg,
    array,
    Categorical,
    set_eng_float_format,
    Series,
    DataFrame,
)

from pandas.core.dtypes.dtypes import SparseDtype

from pandas.tseries.api import infer_freq
from pandas.tseries import offsets

from pandas.core.computation.api import eval

from pandas.core.reshape.api import (
    concat,
    lreshape,
    melt,
    wide_to_long,
    merge,
    merge_asof,
    merge_ordered,
    crosstab,
    pivot,
    pivot_table,
    get_dummies,
    from_dummies,
    cut,
    qcut,
)

from pandas import api, arrays, errors, io, plotting, tseries
from pandas import testing
from pandas.util._print_versions import show_versions

from pandas.io.api import (
    # excel
    ExcelFile,
    ExcelWriter,
    read_excel,
    # parsers
    read_csv,
    read_fwf,
    read_table,
    # pickle
    read_pickle,
    to_pickle,
    # pytables
    HDFStore,
    read_hdf,
    # sql
    read_sql,
    read_sql_query,
    read_sql_table,
    # misc
    read_clipboard,
    read_parquet,
    read_orc,
    read_feather,
    read_gbq,
    read_html,
    read_xml,
    read_json,
    read_stata,
    read_sas,
    read_spss,
)

from pandas.io.json._normalize import json_normalize

from pandas.util._tester import test

# use the closest tagged version if possible
_built_with_meson = False
try:
    from pandas._version_meson import (  # pyright: ignore [reportMissingImports]
        __version__,
        __git_version__,
    )

    _built_with_meson = True
except ImportError:
    from pandas._version import get_versions

    v = get_versions()
    __version__ = v.get("closest-tag", v["version"])
    __git_version__ = v.get("full-revisionid")
    del get_versions, v

# GH#55043 - deprecation of the data_manager option
if "PANDAS_DATA_MANAGER" in os.environ:
    warnings.warn(
        "The env variable PANDAS_DATA_MANAGER is set. The data_manager option is "
        "deprecated and will be removed in a future version. Only the BlockManager "
        "will be available. Unset this environment variable to silence this warning.",
        FutureWarning,
        stacklevel=2,
    )

del warnings, os

# module level doc-string
__doc__ = """
pandas - a powerful data analysis and manipulation library for Python
=====================================================================

**pandas** is a Python package providing fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, **real world** data analysis in Python. Additionally, it has
the broader goal of becoming **the most powerful and flexible open source data
analysis / manipulation tool available in any language**. It is already well on
its way toward this goal.

Main Features
-------------
Here are just a few of the things that pandas does well:

  - Easy handling of missing data in floating point as well as non-floating
    point data.
  - Size mutability: columns can be inserted and deleted from DataFrame and
    higher dimensional objects
  - Automatic and explicit data alignment: objects can be explicitly aligned
    to a set of labels, or the user can simply ignore the labels and let
    `Series`, `DataFrame`, etc. automatically align the data for you in
    computations.
  - Powerful, flexible group by functionality to perform split-apply-combine
    operations on data sets, for both aggregating and transforming data.
  - Make it easy to convert ragged, differently-indexed data in other Python
    and NumPy data structures into DataFrame objects.
  - Intelligent label-based slicing, fancy indexing, and subsetting of large
    data sets.
  - Intuitive merging and joining data sets.
  - Flexible reshaping and pivoting of data sets.
  - Hierarchical labeling of axes (possible to have multiple labels per tick).
  - Robust IO tools for loading data from flat files (CSV and delimited),
    Excel files, databases, and saving/loading data from the ultrafast HDF5
    format.
  - Time series-specific functionality: date range generation and frequency
    conversion, moving window statistics, date shifting and lagging.
"""

# Use __all__ to let type checkers know what is part of the public API.
# Pandas is not (yet) a py.typed library: the public API is determined
# based on the documentation.
__all__ = [
    "ArrowDtype",
    "BooleanDtype",
    "Categorical",
    "CategoricalDtype",
    "CategoricalIndex",
    "DataFrame",
    "DateOffset",
    "DatetimeIndex",
    "DatetimeTZDtype",
    "ExcelFile",
    "ExcelWriter",
    "Flags",
    "Float32Dtype",
    "Float64Dtype",
    "Grouper",
    "HDFStore",
    "Index",
    "IndexSlice",
    "Int16Dtype",
    "Int32Dtype",
    "Int64Dtype",
    "Int8Dtype",
    "Interval",
    "IntervalDtype",
    "IntervalIndex",
    "MultiIndex",
    "NA",
    "NaT",
    "NamedAgg",
    "Period",
    "PeriodDtype",
    "PeriodIndex",
    "RangeIndex",
    "Series",
    "SparseDtype",
    "StringDtype",
    "Timedelta",
    "TimedeltaIndex",
    "Timestamp",
    "UInt16Dtype",
    "UInt32Dtype",
    "UInt64Dtype",
    "UInt8Dtype",
    "api",
    "array",
    "arrays",
    "bdate_range",
    "concat",
    "crosstab",
    "cut",
    "date_range",
    "describe_option",
    "errors",
    "eval",
    "factorize",
    "get_dummies",
    "from_dummies",
    "get_option",
    "infer_freq",
    "interval_range",
    "io",
    "isna",
    "isnull",
    "json_normalize",
    "lreshape",
    "melt",
    "merge",
    "merge_asof",
    "merge_ordered",
    "notna",
    "notnull",
    "offsets",
    "option_context",
    "options",
    "period_range",
    "pivot",
    "pivot_table",
    "plotting",
    "qcut",
    "read_clipboard",
    "read_csv",
    "read_excel",
    "read_feather",
    "read_fwf",
    "read_gbq",
    "read_hdf",
    "read_html",
    "read_json",
    "read_orc",
    "read_parquet",
    "read_pickle",
    "read_sas",
    "read_spss",
    "read_sql",
    "read_sql_query",
    "read_sql_table",
    "read_stata",
    "read_table",
    "read_xml",
    "reset_option",
    "set_eng_float_format",
    "set_option",
    "show_versions",
    "test",
    "testing",
    "timedelta_range",
    "to_datetime",
    "to_numeric",
    "to_pickle",
    "to_timedelta",
    "tseries",
    "unique",
    "value_counts",
    "wide_to_long",
]
