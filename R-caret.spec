#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-caret
Version  : 6.0.78
Release  : 3
URL      : https://cran.r-project.org/src/contrib/caret_6.0-78.tar.gz
Source0  : https://cran.r-project.org/src/contrib/caret_6.0-78.tar.gz
Summary  : Classification and Regression Training
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-caret-lib
Requires: R-Cubist
Requires: R-ModelMetrics
Requires: R-earth
Requires: R-ggplot2
Requires: R-klaR
Requires: R-pamr
Requires: R-pls
Requires: R-recipes
Requires: R-spls
Requires: R-subselect
Requires: R-superpc
Requires: R-withr
BuildRequires : R-Cubist
BuildRequires : R-ModelMetrics
BuildRequires : R-earth
BuildRequires : R-ggplot2
BuildRequires : R-klaR
BuildRequires : R-pamr
BuildRequires : R-pls
BuildRequires : R-recipes
BuildRequires : R-spls
BuildRequires : R-subselect
BuildRequires : R-superpc
BuildRequires : R-withr
BuildRequires : clr-R-helpers

%description
regression models.

%package lib
Summary: lib components for the R-caret package.
Group: Libraries

%description lib
lib components for the R-caret package.


%prep
%setup -q -c -n caret

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521305123

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521305123
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caret
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caret
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caret
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library caret|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
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
/usr/lib64/R/library/caret/doc/caret.Rnw
/usr/lib64/R/library/caret/doc/caret.pdf
/usr/lib64/R/library/caret/doc/index.html
/usr/lib64/R/library/caret/help/AnIndex
/usr/lib64/R/library/caret/help/aliases.rds
/usr/lib64/R/library/caret/help/caret.rdb
/usr/lib64/R/library/caret/help/caret.rdx
/usr/lib64/R/library/caret/help/paths.rds
/usr/lib64/R/library/caret/html/00Index.html
/usr/lib64/R/library/caret/html/R.css
/usr/lib64/R/library/caret/libs/symbols.rds
/usr/lib64/R/library/caret/models/models.RData
/usr/lib64/R/library/caret/models/sampling.RData

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/caret/libs/caret.so
/usr/lib64/R/library/caret/libs/caret.so.avx2
/usr/lib64/R/library/caret/libs/caret.so.avx512
