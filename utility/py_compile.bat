@echo off

REM -*- coding: utf-8 -*-

REM Copyright (C) 2018  Daniele Giudice
REM This program is free software: you can redistribute it and/or modify
REM it under the terms of the GNU General Public License as published by
REM the Free Software Foundation, either version 3 of the License, or
REM (at your option) any later version.
REM This program is distributed in the hope that it will be useful,
REM but WITHOUT ANY WARRANTY; without even the implied warranty of
REM MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM GNU General Public License for more details.
REM You should have received a copy of the GNU General Public License
REM along with this program.  If not, see http://www.gnu.org/licenses/

REM Compile a file passed by argument automatically

python -c "import glob, os, shutil, sys, py_compile; py_compile.compile(sys.argv[1]); n=os.path.split(os.path.abspath(sys.argv[1]))[1]; p=os.path.split(os.path.abspath(sys.argv[1]))[0]; shutil.copy2(glob.glob(os.path.join(p, '__pycache__', '*.pyc'), recursive=False)[0], os.path.join(p, '{}c'.format(n)); shutil.rmtree(os.path.join(p, '__pycache__'))"

pause