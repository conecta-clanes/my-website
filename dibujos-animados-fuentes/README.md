#pip install pygame pillow opencv-python numpy music

py main.py

#py -m pip install -upgrade pip

# Valor por defecto (160)
python main.py                                                                                                        
# Escenario casi paco                                                                                                  python main.py --bg-alpha 240

# Escenario muy transparente
python main.py --bg-alpha 60

# Ver ayuda
python main.py --help

  # Solo previsualización (por defecto)
  python main.py                                                                                                        
  # Con grabación de Video                                                                                                python main.py 
  
  --grabar

  # Combinado con transparencia
  python main.py --grabar --bg-alpha 220