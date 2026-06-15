import os
import subprocess

def run_script(script_path):
    print(f"\n🚀 Running: {script_path}...")
    try:
        subprocess.run(['python', script_path], check=True)
        print(f"✅ Success!")
    except subprocess.CalledProcessError:
        print(f"❌ Error running {script_path}. Halting pipeline.")
        exit(1)

if __name__ == "__main__":
    print("🌟 BLUESTOCK FINTECH: STARTING ANALYTICS PIPELINE 🌟")
    print("Note: Core ETL and computations were executed via Jupyter Notebooks.")
    
    # Updated to match your exact file structure from the screenshots!
    scripts_to_run = [
        'live_nav_fetch.py',
        'notebooks/recommender.py'
    ]
    
    for script in scripts_to_run:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"⚠️ Could not find {script}. Skipping...")
            
    print("\n🎉 Pipeline execution complete! Data is ready for the Power BI Dashboard.")