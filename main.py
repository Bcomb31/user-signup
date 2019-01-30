from flask import Flask, request, redirect
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')