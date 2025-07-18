Instructions to run

1. Clone the repository
git clone https://github.com/your-username/todo-app.git
cd todo-app

 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

 3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Start the server
python manage.py runserver
