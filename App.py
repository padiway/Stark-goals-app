from flask import Flask, render_template_string, request

app = Flask(__name__)

# Configuración del código de descuento
CODIGO_DESCUENTO = "STARKBET"
USOS_MAXIMOS = 20
usos_actuales = 0

# HTML con diseño azul oscuro y profesional
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Stark Goals VIP 🌌</title>
    <style>
        body {
            background-color: #0a0a23;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1, h2 {
            color: #00ccff;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: #111;
        }
        th, td {
            border: 1px solid #444;
            padding: 10px;
            text-align: center;
        }
        a.btn {
            background-color: #008CBA;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }
        a.whatsapp-btn {
            background-color: #25D366;
            color: white;
            padding: 12px 20px;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
            display: inline-block;
            margin-top: 20px;
        }
        form {
            background-color: #111;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        input[type="text"], input[type="email"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border: none;
        }
        input[type="submit"] {
            background-color: #00ccff;
            color: #000;
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }
        .mensaje {
            margin: 15px 0;
            font-weight: bold;
            font-size: 1.1em;
        }
        .ok { color: #00ff88; }
        .error { color: #ff4d4d; }
    </style>
</head>
<body>
    <h1>🌌 Stark Goals VIP 🌌</h1>
    <p>Tu sistema profesional de apuestas deportivas con resultados comprobados.</p>

    <h2>🙌 Únete a la comunidad:</h2>
    <form method="POST">
        <input type="text" name="nombre" placeholder="Tu nombre" required>
        <input type="email" name="correo" placeholder="Tu correo" required>
        <input type="text" name="codigo" placeholder="Código de descuento (opcional)">
        <input type="submit" value="Aplicar Código y Ver Precios">
    </form>

    {% if mensaje %}
    <p class="mensaje {{ clase }}">{{ mensaje }}</p>
    {% endif %}

    <h2>💰 Planes disponibles:</h2>
    <table>
        <tr>
            <th>Plan</th>
            <th>Duración</th>
            <th>Precio</th>
            <th>Pagar</th>
        </tr>
        <tr>
            <td>Mensual</td>
            <td>1 mes</td>
            <td>${{ mensual }} COP</td>
            <td><a href="{{ link_mensual }}" class="btn">Pagar</a></td>
        </tr>
        <tr>
            <td>Trimestral</td>
            <td>3 meses</td>
            <td>${{ trimestral }} COP</td>
            <td><a href="{{ link_trimestral }}" class="btn">Pagar</a></td>
        </tr>
        <tr>
            <td>Semestral</td>
            <td>6 meses</td>
            <td>${{ semestral }} COP</td>
            <td><a href="{{ link_semestral }}" class="btn">Pagar</a></td>
        </tr>
        <tr>
            <td>Anual</td>
            <td>12 meses</td>
            <td>${{ anual }} COP</td>
            <td><a href="{{ link_anual }}" class="btn">Pagar</a></td>
        </tr>
    </table>

    <h2>📲 Métodos de pago alternativos:</h2>
    <p><strong>Nequi / Daviplata:</strong> 3117776320 (Daniel Padilla Marimón)</p>
    <p><strong>PayPal:</strong> danielpadilla152018@gmail.com</p>

    <h2>🧠 ¿Qué obtienes con tu suscripción?</h2>
    <ul>
        <li>✔ Acceso exclusivo al grupo <strong>Stark Goals VIP</strong></li>
        <li>✔ Análisis estadístico profesional con más de 300 apuestas comprobadas</li>
        <li>✔ Enfoque en rentabilidad a largo plazo</li>
        <li>✔ Alertas diarias de valor y estrategias seguras</li>
    </ul>

    <a href="https://wa.me/573117776320" class="whatsapp-btn">📲 Contáctame por WhatsApp</a>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def inicio():
    global usos_actuales

    precios = {
        "mensual": 65000,
        "trimestral": 177000,
        "semestral": 390000,
        "anual": 790000
    }

    links = {
        "mensual": "https://onetouch.astropay.com/payment?external_reference_id=yQhLPb2z0AxcipNOmAz9PMvcclXU1yU9",
        "trimestral": "https://onetouch.astropay.com/payment?external_reference_id=FIKYIzFSVKBBtyb8nXc5RxBOia5SwsQJ",
        "semestral": "https://onetouch.astropay.com/payment?external_reference_id=dlrDIgquJRYEFAHZkN3wipC3Y8ekQHGV",
        "anual": "https://onetouch.astropay.com/payment?external_reference_id=TByrspBzhDYFcCYSvXoqq8s04YBvb7YO"
    }

    mensaje = ""
    clase = ""

    if request.method == 'POST':
        codigo = request.form.get('codigo', '').strip().upper()

        if codigo == CODIGO_DESCUENTO:
            if usos_actuales < USOS_MAXIMOS:
                for k in precios:
                    precios[k] = int(precios[k] * 0.8)
                usos_actuales += 1
                mensaje = f"✅ ¡Descuento aplicado! Código válido para las primeras {USOS_MAXIMOS} personas. Te quedan {USOS_MAXIMOS - usos_actuales} usos disponibles."
                clase = "ok"
            else:
                mensaje = "❌ El código STARKBET ya fue usado por 20 personas."
                clase = "error"
        elif codigo != "":
            mensaje = "⚠️ Código inválido. Asegúrate de escribirlo correctamente."
            clase = "error"

    return render_template_string(html,
                                  mensaje=mensaje,
                                  clase=clase,
                                  mensual=precios["mensual"],
                                  trimestral=precios["trimestral"],
                                  semestral=precios["semestral"],
                                  anual=precios["anual"],
                                  link_mensual=links["mensual"],
                                  link_trimestral=links["trimestral"],
                                  link_semestral=links["semestral"],
                                  link_anual=links["anual"])

if __name__ == '__main__':
    app.run(debug=True)
