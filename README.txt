Title Parkinsons mixed symptom simulation

What this project does
This single Python file simulates three symptom types associated with Parkinsons disease tremor rigidity and slowness. It runs a short time series for each symptom and computes a simple probability like score from those simulated means plus user inputs.

Inputs used
age in years
sleep hours per night
self reported symptom score from 0 to 10

How the simulation works
Each symptom is represented by a small time series of 10 steps. Each step increases slowly by a growth term and includes some random noise. The program computes mean values for each symptom. A weighted formula combines the mean tremor rigidity and slowness values using weights 0.4 0.3 0.3 and mixes this with the self reported symptom score. Age and sleep factors adjust the result. Final probability is scaled between 0 and 100 percent.

Why this is valid for the course
The code uses only basic Python concepts covered in the program lists loops conditionals functions the random module and printing. No external libraries or advanced methods are used.

How to run
Open terminal or VS Code terminal in the project folder. Run
python main.py
Follow prompts and read printed results.

Disclaimer
This is an educational simulation not a medical tool. Do not use results for diagnosis.