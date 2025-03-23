# flask_socketIO_print_app
Bu proje, Flask-SocketIO kullanarak gerçek zamanlı veri iletimi sağlayan basit bir Flask uygulamasıdır. Kullanıcıların giriş yapmasını sağlar ve veritabanı olarak SQLite kullanır.

# Depoyu Klonlayın
git clone https://github.com/mertalidincer/flask_socketIO_print_app.git
cd flask_socketIO_print_app

# Sanal Ortamı Oluşturun ve Bağlayın
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
# veya
.venv\Scripts\activate  # Windows

# Bağımlılıkları Yükleyin
pip install -r requirements.txt

# Veritabanını Başlatın
flask init-db

# Uygulamayı Çalıştırın
python app.py
