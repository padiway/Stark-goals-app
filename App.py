from flask import Flask, render_template_string

app = Flask(__name__)

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
        a.whatsapp-btn {
            display: inline-block;
            background-color: #25D366;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
            margin-top: 20px;
        }
        a.payment-link {
            display: block;
            margin: 10px 0;
            color: #00ffcc;
        }
    </style>
</head>
<body>
    <h1>🌌 Stark Goals VIP 🌌</h1>
    <p>Tu sistema profesional de apuestas deportivas con resultados comprobados.</p>

    <h2>💰 Planes disponibles:</h2>
    <table>
        <tr>
            <th>Plan</th><th>Duración</th><th>Precio</th>
        </tr>
        <tr>
            <td>Mensual</td><td>1 mes</td><td>$65,000 COP</td>
        </tr>
        <tr>
            <td>Trimestral</td><td>3 meses</td><td>$177,000 COP</td>
        </tr>
        <tr>
            <td>Semestral</td><td>6 meses</td><td>$390,000 COP</td>
        </tr>
        <tr>
            <td>Anual</td><td>12 meses</td><td>$790,000 COP</td>
        </tr>
    </table>

    <h2>📲 Métodos de pago:</h2>
    <p><strong>Nequi / Daviplata:</strong> 3117776320 (Daniel Padilla Marimón)</p>
    <p><strong>PayPal:</strong> <a href="mailto: danielpadilla152018@gmail.com">danielpadilla152018@gmail.com</a></p>

    <h3>💸 Pagos con AstroPay:</h3>
    <a class="payment-link" href="https://onetouch.astropay.com/payment?external_reference_id=yQhLPb2z0AxcipNOmAz9PMvcclXU1yU9" target="_blank">Mensual - $65,000</a>
    <a class="payment-link" href="https://onetouch.astropay.com/payment?external_reference_id=FIKYIzFSVKBBtyb8nXc5RxBOia5SwsQJ" target="_blank">Trimestral - $177,000</a>
    <a class="payment-link" href="https://onetouch.astropay.com/payment?external_reference_id=dlrDIgquJRYEFAHZkN3wipC3Y8ekQHGV" target="_blank">Semestral - $390,000</a>
    <a class="payment-link" href="https://onetouch.astropay.com/payment?external_reference_id=TByrspBzhDYFcCYSvXoqq8s04YBvb7YO" target="_blank">Anual - $790,000</a>

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

@app.route('/')
def inicio():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
