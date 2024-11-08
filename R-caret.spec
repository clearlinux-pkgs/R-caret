#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-caret
Version  : 6.0.94
Release  : 74
URL      : https://cran.r-project.org/src/contrib/caret_6.0-94.tar.gz
Source0  : https://cran.r-project.org/src/contrib/caret_6.0-94.tar.gz
Summary  : Classification and Regression Training
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-caret-lib = %{version}-%{release}
Requires: R-ModelMetrics
Requires: R-e1071
Requires: R-foreach
Requires: R-ggplot2
Requires: R-pROC
Requires: R-plyr
Requires: R-recipes
Requires: R-reshape2
Requires: R-withr
BuildRequires : R-ModelMetrics
BuildRequires : R-e1071
BuildRequires : R-fastICA
BuildRequires : R-foreach
BuildRequires : R-ggplot2
BuildRequires : R-pROC
BuildRequires : R-plyr
BuildRequires : R-recipes
BuildRequires : R-reshape2
BuildRequires : R-themis
BuildRequires : R-withr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
regression models.

%package lib
Summary: lib components for the R-caret package.
Group: Libraries

%description lib
lib components for the R-caret package.


%prep
%setup -q -n caret
cd %{_builddir}/caret

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679502763

%install
export SOURCE_DATE_EPOCH=1679502763
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/caret/CITATION
/usr/lib64/R/library/caret/DESCRIPTION
/usr/lib64/R/library/caret/INDEX
/usr/lib64/R/library/caret/Meta/Rd.rds
/usr/lib64/R/library/caret/Meta/data.rds
/usr/lib64/R/library/caret/Meta/features.rds
/usr/lib64/R/library/caret/Meta/hsearch.rds
/usr/lib64/R/library/caret/Meta/links.rds
/usr/lib64/R/library/caret/Meta/nsInfo.rds
/usr/lib64/R/library/caret/Meta/package.rds
/usr/lib64/R/library/caret/Meta/vignette.rds
/usr/lib64/R/library/caret/NAMESPACE
/usr/lib64/R/library/caret/NEWS.Rd
/usr/lib64/R/library/caret/R/caret
/usr/lib64/R/library/caret/R/caret.rdb
/usr/lib64/R/library/caret/R/caret.rdx
/usr/lib64/R/library/caret/data/BloodBrain.RData
/usr/lib64/R/library/caret/data/GermanCredit.RData
/usr/lib64/R/library/caret/data/Sacramento.RData
/usr/lib64/R/library/caret/data/cars.RData
/usr/lib64/R/library/caret/data/cox2.RData
/usr/lib64/R/library/caret/data/datalist
/usr/lib64/R/library/caret/data/dhfr.RData
/usr/lib64/R/library/caret/data/mdrr.RData
/usr/lib64/R/library/caret/data/oil.RData
/usr/lib64/R/library/caret/data/pottery.RData
/usr/lib64/R/library/caret/data/scat.RData
/usr/lib64/R/library/caret/data/segmentationData.RData
/usr/lib64/R/library/caret/data/tecator.RData
/usr/lib64/R/library/caret/doc/caret.R
/usr/lib64/R/library/caret/doc/caret.Rmd
/usr/lib64/R/library/caret/doc/caret.html
/usr/lib64/R/library/caret/doc/index.html
/usr/lib64/R/library/caret/help/AnIndex
/usr/lib64/R/library/caret/help/aliases.rds
/usr/lib64/R/library/caret/help/caret.rdb
/usr/lib64/R/library/caret/help/caret.rdx
/usr/lib64/R/library/caret/help/paths.rds
/usr/lib64/R/library/caret/html/00Index.html
/usr/lib64/R/library/caret/html/R.css
/usr/lib64/R/library/caret/models/models.RData
/usr/lib64/R/library/caret/models/sampling.RData
/usr/lib64/R/library/caret/tests/testthat.R
/usr/lib64/R/library/caret/tests/testthat/test_BoxCox.R
/usr/lib64/R/library/caret/tests/testthat/test_Dummies.R
/usr/lib64/R/library/caret/tests/testthat/test_bad_class_options.R
/usr/lib64/R/library/caret/tests/testthat/test_classDist.R
/usr/lib64/R/library/caret/tests/testthat/test_confusionMatrix.R
/usr/lib64/R/library/caret/tests/testthat/test_data_spliting.R
/usr/lib64/R/library/caret/tests/testthat/test_gafs.R
/usr/lib64/R/library/caret/tests/testthat/test_ggplot.R
/usr/lib64/R/library/caret/tests/testthat/test_glmnet_varImp.R
/usr/lib64/R/library/caret/tests/testthat/test_minimal.R
/usr/lib64/R/library/caret/tests/testthat/test_misc.R
/usr/lib64/R/library/caret/tests/testthat/test_mnLogLoss.R
/usr/lib64/R/library/caret/tests/testthat/test_models_bagEarth.R
/usr/lib64/R/library/caret/tests/testthat/test_multiclassSummary.R
/usr/lib64/R/library/caret/tests/testthat/test_nearZeroVar.R
/usr/lib64/R/library/caret/tests/testthat/test_preProcess.R
/usr/lib64/R/library/caret/tests/testthat/test_preProcess_internals.R
/usr/lib64/R/library/caret/tests/testthat/test_preProcess_methods.R
/usr/lib64/R/library/caret/tests/testthat/test_ptypes.R
/usr/lib64/R/library/caret/tests/testthat/test_recipe_fs.R
/usr/lib64/R/library/caret/tests/testthat/test_recipe_upsample.R
/usr/lib64/R/library/caret/tests/testthat/test_resamples.R
/usr/lib64/R/library/caret/tests/testthat/test_safs.R
/usr/lib64/R/library/caret/tests/testthat/test_sampling_options.R
/usr/lib64/R/library/caret/tests/testthat/test_sparse_Matrix.R
/usr/lib64/R/library/caret/tests/testthat/test_spatialSign.R
/usr/lib64/R/library/caret/tests/testthat/test_tibble.R
/usr/lib64/R/library/caret/tests/testthat/test_twoClassSummary.R
/usr/lib64/R/library/caret/tests/testthat/test_updates.R
/usr/lib64/R/library/caret/tests/testthat/test_varImp.R
/usr/lib64/R/library/caret/tests/testthat/trim.R
/usr/lib64/R/library/caret/tests/testthat/trim_C5.R
/usr/lib64/R/library/caret/tests/testthat/trim_bayesglm.R
/usr/lib64/R/library/caret/tests/testthat/trim_glm.R
/usr/lib64/R/library/caret/tests/testthat/trim_glmnet.R
/usr/lib64/R/library/caret/tests/testthat/trim_rpart.R
/usr/lib64/R/library/caret/tests/testthat/trim_train.R
/usr/lib64/R/library/caret/tests/testthat/trim_treebag.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/caret/libs/caret.so
/usr/lib64/R/library/caret/libs/caret.so.avx2
/usr/lib64/R/library/caret/libs/caret.so.avx512
