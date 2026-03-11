\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{clgrammar}[2026/03/09 Cleaner Conlang / tutorial book class]

% Pass all options through to book
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass{book}

% -----------------------------------------------------------------------------
% Required packages
% -----------------------------------------------------------------------------
\RequirePackage{iftex}
\ifPDFTeX
  \ClassError{clgrammar}{This class requires XeLaTeX or LuaLaTeX}{%
    You loaded fontspec-dependent code. Compile with XeLaTeX or LuaLaTeX.}
\fi

\RequirePackage{fontspec}
\RequirePackage{xcolor}
\RequirePackage[
  paper=a4paper,
  inner=28mm,
  outer=24mm,
  top=28mm,
  bottom=28mm,
  headheight=15pt,
  headsep=10pt,
  footskip=14mm
]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{titling}
\RequirePackage[
  bookmarks=true,
  bookmarksopen=true,
  bookmarksnumbered=true,
  pdfstartview=FitH,
  colorlinks=false,
  linkbordercolor=red,
  citebordercolor=red,
  urlbordercolor=red,
  pdfborder={0 0 1}
]{hyperref}
\RequirePackage{titlesec}
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{verbatim}
\RequirePackage{tcolorbox}
\tcbuselibrary{listingsutf8}
\RequirePackage{fvextra}
\RequirePackage{float}
\RequirePackage{placeins}
\RequirePackage{forest}
\RequirePackage{listings}
\RequirePackage{pdflscape}
\RequirePackage{longtable}
\RequirePackage{environ}
\RequirePackage[draft]{minted}
\RequirePackage{anyfontsize}
\RequirePackage{multirow}
\RequirePackage{tabularx}
\RequirePackage{booktabs}
\RequirePackage{makecell}

% -----------------------------------------------------------------------------
% Engine check and fonts
% -----------------------------------------------------------------------------
% already handled above before fontspec

% -----------------------------------------------------------------------------
% Core appearance
% -----------------------------------------------------------------------------
\definecolor{chapter}{rgb}{0.2, 0.25, 0.4}
\definecolor{section}{rgb}{0.2, 0.45, 0.3}
\definecolor{cover}{RGB}{0, 120, 60}
\definecolor{background}{rgb}{1.0, 0.99, 0.95}

\newcommand{\headlinecolor}{\normalcolor}

% -----------------------------------------------------------------------------
% Layout and page style
% -----------------------------------------------------------------------------
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\renewcommand{\chaptermark}[1]{\markboth{Session \thechapter\enspace #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\enspace #1}}

\fancyhead[LE]{\nouppercase{\leftmark}}
\fancyhead[RO]{\nouppercase{\rightmark}}
\fancyfoot[C]{\thepage}

% Make chapter opening pages consistent with the rest of the document.
\fancypagestyle{plain}{%
  \fancyhf{}
  \renewcommand{\headrulewidth}{0.4pt}
  \fancyhead[LE]{\nouppercase{\leftmark}}
  \fancyhead[RO]{\nouppercase{\rightmark}}
  \fancyfoot[C]{\thepage}
}

% -----------------------------------------------------------------------------
% Section and chapter headings
% -----------------------------------------------------------------------------
\titleformat{\chapter}[display]
  {\normalfont\bfseries\color{chapter}}
  {\filleft\Large Session \thechapter}
  {0.8ex}
  {\titlerule[0.8pt]\vspace{1ex}\filright\Huge}
  [\vspace{1ex}\titlerule]

\titlespacing*{\chapter}{0pt}{0pt}{2.5ex}

\titleformat{\section}
  {\normalfont\Large\bfseries\color{section}}
  {Section \thesection}{0.75em}{}

\titleformat{\subsection}
  {\normalfont\large\bfseries}
  {\thesubsection}{0.75em}{}

% -----------------------------------------------------------------------------
% Lecturer toggle
% -----------------------------------------------------------------------------
\newif\iflecturer
\lecturertrue
% \lecturerfalse

\iflecturer
  \newtcolorbox{lectureronly}{
    colback=yellow!10!white,
    colframe=yellow!50!black,
    title=Lecturer Only Content,
    fonttitle=\bfseries,
    fontupper=\small\itshape
  }
\else
  \newtcolorbox{lectureronly}{
    visible=false,
    height=0pt,
    left=0pt, right=0pt, top=0pt, bottom=0pt, boxsep=0pt,
    boxrule=0pt, colframe=white, colback=white
  }
\fi

% -----------------------------------------------------------------------------
% Title page helpers
% -----------------------------------------------------------------------------
\newcommand{\booksubtitle}{2025/2026}
\newcommand{\subtitle}[1]{\renewcommand{\booksubtitle}{#1}}
\newcommand{\HUGE}{\fontsize{40}{48}\selectfont}

\renewcommand{\maketitle}{%
  \begin{titlepage}
    \pagecolor{cover}%
    \color{white}%
    \thispagestyle{empty}%
    \begin{center}
      \vspace*{0.12\textheight}
      {\HUGE\bfseries\textsc{\thetitle}\par}
      \vspace{0.8cm}
      {\Large\itshape \booksubtitle\par}
      \vfill
      {\Large \theauthor\par}
      \vspace*{0.08\textheight}
    \end{center}
  \end{titlepage}%
  \clearpage
  \pagecolor{background}%
}

% -----------------------------------------------------------------------------
% Simple boxed gloss environment
% -----------------------------------------------------------------------------
\newenvironment{gloss}
  {%
    \par\medskip
    \begin{center}
    \begin{tabular}{|p{0.9\linewidth}|}
    \hline
    \ignorespaces
  }
  {%
    \unskip\\\hline
    \end{tabular}
    \end{center}
    \par\medskip
  }

\endinput