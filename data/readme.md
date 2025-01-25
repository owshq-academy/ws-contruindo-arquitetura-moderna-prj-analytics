# Step 1: Clone the repository
git clone https://github.com/owshq-academy/ws-contruindo-arquitetura-moderna-dados-prj-analytics.git
cd ws-contruindo-arquitetura-moderna-dados-prj-analytics

# Step 2: Create a virtual environment
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv

# Step 3: Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Save new dependencies (if adding more libraries)
pip freeze > requirements.txt


