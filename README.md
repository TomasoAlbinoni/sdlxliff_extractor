# sdlxliff_extractor
Extract source file that is embedded in sdlxliff

Sdlxliff files contain a base64-encoded zipped version of the source file.
This Python script extracts that zip file. Usage:

> python decode.py example.sdlxliff [example2.sdlxliff [example3.sdlxliff...]]
