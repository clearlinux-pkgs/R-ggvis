#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggvis
Version  : 0.4.5
Release  : 23
URL      : https://cran.r-project.org/src/contrib/ggvis_0.4.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggvis_0.4.5.tar.gz
Summary  : Interactive Grammar of Graphics
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1 MIT
Requires: R-assertthat
Requires: R-dplyr
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-lazyeval
Requires: R-magrittr
Requires: R-plyr
Requires: R-shiny
BuildRequires : R-assertthat
BuildRequires : R-dplyr
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-magrittr
BuildRequires : R-plyr
BuildRequires : R-shiny
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# ggvis
[![Build Status](https://travis-ci.org/rstudio/ggvis.svg?branch=master)](https://travis-ci.org/rstudio/ggvis)

%prep
%setup -q -c -n ggvis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572107040

%install
export SOURCE_DATE_EPOCH=1572107040
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggvis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggvis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggvis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ggvis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggvis/DESCRIPTION
/usr/lib64/R/library/ggvis/INDEX
/usr/lib64/R/library/ggvis/LICENSE
/usr/lib64/R/library/ggvis/Meta/Rd.rds
/usr/lib64/R/library/ggvis/Meta/data.rds
/usr/lib64/R/library/ggvis/Meta/demo.rds
/usr/lib64/R/library/ggvis/Meta/features.rds
/usr/lib64/R/library/ggvis/Meta/hsearch.rds
/usr/lib64/R/library/ggvis/Meta/links.rds
/usr/lib64/R/library/ggvis/Meta/nsInfo.rds
/usr/lib64/R/library/ggvis/Meta/package.rds
/usr/lib64/R/library/ggvis/NAMESPACE
/usr/lib64/R/library/ggvis/NEWS.md
/usr/lib64/R/library/ggvis/R/ggvis
/usr/lib64/R/library/ggvis/R/ggvis.rdb
/usr/lib64/R/library/ggvis/R/ggvis.rdx
/usr/lib64/R/library/ggvis/data/Rdata.rdb
/usr/lib64/R/library/ggvis/data/Rdata.rds
/usr/lib64/R/library/ggvis/data/Rdata.rdx
/usr/lib64/R/library/ggvis/demo/bar.r
/usr/lib64/R/library/ggvis/demo/boxplot.r
/usr/lib64/R/library/ggvis/demo/brush.r
/usr/lib64/R/library/ggvis/demo/dynamic.r
/usr/lib64/R/library/ggvis/demo/guides.r
/usr/lib64/R/library/ggvis/demo/histogram.r
/usr/lib64/R/library/ggvis/demo/hover.r
/usr/lib64/R/library/ggvis/demo/interactive.R
/usr/lib64/R/library/ggvis/demo/lines.r
/usr/lib64/R/library/ggvis/demo/scales.r
/usr/lib64/R/library/ggvis/demo/scatterplot.r
/usr/lib64/R/library/ggvis/demo/size.r
/usr/lib64/R/library/ggvis/demo/smooth.r
/usr/lib64/R/library/ggvis/demo/subvis.R
/usr/lib64/R/library/ggvis/demo/tile.r
/usr/lib64/R/library/ggvis/demo/tourr.r
/usr/lib64/R/library/ggvis/help/AnIndex
/usr/lib64/R/library/ggvis/help/aliases.rds
/usr/lib64/R/library/ggvis/help/ggvis.rdb
/usr/lib64/R/library/ggvis/help/ggvis.rdx
/usr/lib64/R/library/ggvis/help/paths.rds
/usr/lib64/R/library/ggvis/html/00Index.html
/usr/lib64/R/library/ggvis/html/R.css
/usr/lib64/R/library/ggvis/tests/specs/bar.r
/usr/lib64/R/library/ggvis/tests/specs/bar/categorical-x.json
/usr/lib64/R/library/ggvis/tests/specs/bar/continuous-x.json
/usr/lib64/R/library/ggvis/tests/specs/boxplot.r
/usr/lib64/R/library/ggvis/tests/specs/boxplot/boxplot-categorical.json
/usr/lib64/R/library/ggvis/tests/specs/boxplot/boxplot-continuous.json
/usr/lib64/R/library/ggvis/tests/specs/boxplot/boxplot-no-outliers.json
/usr/lib64/R/library/ggvis/tests/specs/data.r
/usr/lib64/R/library/ggvis/tests/specs/data/dots.json
/usr/lib64/R/library/ggvis/tests/specs/layer.r
/usr/lib64/R/library/ggvis/tests/specs/layer/freqpoly-grouped.json
/usr/lib64/R/library/ggvis/tests/specs/layer/histogram.json
/usr/lib64/R/library/ggvis/tests/specs/layer/smooth-grouped.json
/usr/lib64/R/library/ggvis/tests/specs/layer/smooth.json
/usr/lib64/R/library/ggvis/tests/specs/line.r
/usr/lib64/R/library/ggvis/tests/specs/line/basic.json
/usr/lib64/R/library/ggvis/tests/specs/line/layer-line-nominal-x.json
/usr/lib64/R/library/ggvis/tests/specs/line/layer-line.json
/usr/lib64/R/library/ggvis/tests/specs/line/sort.json
/usr/lib64/R/library/ggvis/tests/specs/scales.R
/usr/lib64/R/library/ggvis/tests/specs/scales/bars.json
/usr/lib64/R/library/ggvis/tests/specs/scales/combined_legend.json
/usr/lib64/R/library/ggvis/tests/specs/scales/custom.json
/usr/lib64/R/library/ggvis/tests/specs/scales/datetime.json
/usr/lib64/R/library/ggvis/tests/specs/scales/datetime_hist.json
/usr/lib64/R/library/ggvis/tests/specs/scales/domain_numeric.json
/usr/lib64/R/library/ggvis/tests/specs/scales/dual.json
/usr/lib64/R/library/ggvis/tests/specs/scales/hide_guides.json
/usr/lib64/R/library/ggvis/tests/specs/scales/log.json
/usr/lib64/R/library/ggvis/tests/specs/scatter.r
/usr/lib64/R/library/ggvis/tests/specs/scatter/basic.json
/usr/lib64/R/library/ggvis/tests/specs/scatter/fill-continuous.json
/usr/lib64/R/library/ggvis/tests/specs/scatter/fill-discrete.json
/usr/lib64/R/library/ggvis/tests/specs/scatter/transform.json
/usr/lib64/R/library/ggvis/tests/testthat.R
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-bin.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-boxplot.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-count.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-density.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-model-prediction.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-stack.r
/usr/lib64/R/library/ggvis/tests/testthat/test-compute-tabulate.r
/usr/lib64/R/library/ggvis/tests/testthat/test-flatten.r
/usr/lib64/R/library/ggvis/tests/testthat/test-ggvis.R
/usr/lib64/R/library/ggvis/tests/testthat/test-is-dynamic.r
/usr/lib64/R/library/ggvis/tests/testthat/test-mark-properties.r
/usr/lib64/R/library/ggvis/tests/testthat/test-props.r
/usr/lib64/R/library/ggvis/tests/testthat/test-specs.r
/usr/lib64/R/library/ggvis/tests/testthat/test-utils-data.r
/usr/lib64/R/library/ggvis/tests/testthat/test-utils.r
/usr/lib64/R/library/ggvis/update.sh
/usr/lib64/R/library/ggvis/www/ggvis/css/gear.png
/usr/lib64/R/library/ggvis/www/ggvis/css/ggvis.css
/usr/lib64/R/library/ggvis/www/ggvis/js/ggvis.js
/usr/lib64/R/library/ggvis/www/ggvis/js/shiny-ggvis.js
/usr/lib64/R/library/ggvis/www/lib/d3/d3.js
/usr/lib64/R/library/ggvis/www/lib/d3/d3.min.js
/usr/lib64/R/library/ggvis/www/lib/detect-resize/jquery.resize.js
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_diagonals-thick_18_b81900_40x40.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_diagonals-thick_20_666666_40x40.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_flat_10_000000_40x100.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_glass_100_f6f6f6_1x400.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_glass_100_fdf5ce_1x400.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_glass_65_ffffff_1x400.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_gloss-wave_35_f6a828_500x100.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_highlight-soft_100_eeeeee_1x100.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-bg_highlight-soft_75_ffe45c_1x100.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-icons_222222_256x240.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-icons_228ef1_256x240.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-icons_ef8c08_256x240.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-icons_ffd27a_256x240.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/images/ui-icons_ffffff_256x240.png
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/index.html
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.css
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.js
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.min.css
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.min.js
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.structure.css
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.structure.min.css
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.theme.css
/usr/lib64/R/library/ggvis/www/lib/jquery-ui/jquery-ui.theme.min.css
/usr/lib64/R/library/ggvis/www/lib/jquery/AUTHORS.txt
/usr/lib64/R/library/ggvis/www/lib/jquery/jquery.js
/usr/lib64/R/library/ggvis/www/lib/jquery/jquery.min.js
/usr/lib64/R/library/ggvis/www/lib/lodash/lodash.min.js
/usr/lib64/R/library/ggvis/www/lib/vega/vega.js
/usr/lib64/R/library/ggvis/www/lib/vega/vega.min.js
