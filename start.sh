#!/bin/bash

cd backend && source venv/bin/activate
open -a Terminal.app python app_api.py
cd ../frontend/react/scrum-master-frontend 
exec npm install
exec npm start &
