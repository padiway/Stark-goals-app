from flask import Flask, render_template_string, request

app = Flask(__name__)

DESCUENTO_CODIGO = "STARKBET"
USOS_DISPONIBLES = 20
usos_actuales = 0

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Stark Goals</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #0a0a0a; color: #fff; }
        header { background: #111; padding: 20px; text-align: center; }
        h1 { margin: 0; font-size: 2em; }
        section { padding: 20px; }
        .beneficio, .plan { margin-bottom: 15px; background: #1a1a1a; padding: 15px; border-radius: 8px; }
        form { background: #1a1a1a; padding: 20px; border-radius: 8px; margin-top: 30px; }
        input[type="text"], input[type="email"] {
            width: 100%; padding: 10px; margin-bottom: 10px; border: none; border-radius: 5px;
        }
        input[type="submit"] {
            background: #e50914; color: #fff; border: none; padding: 10px 20px; border-radius: 5px;
            cursor: pointer;
        }
        .footer { text-align: center; font-size: 0.8em; color: #aaa; margin-top: 50px; }
        .descuento { color: #0f0; font-weight: bold; }
        .error { color: #f33; font-weight: bold; }
    </style>
</head>
<body>
    <header>
        <h1>🔥 Stark Goals 🔥</h1>
        <p>Tu nueva comunidad de predicciones deportivas inteligentes</p>
    </header>

    <section>
        <h2>¿Por qué unirte?</h2>
        <div class="beneficio">✅ Estadísticas en tiempo real</div>
        <div class="beneficio">✅ Cuotas de valor diario</div>
        <div class="beneficio">✅ Comunidad privada y soporte personalizado</div>
    </section>

    <section>
        <h2>💌 Únete con tu correo y obtén beneficios</h2>
        <form method="POST" action="/">
            <input type="text" name="nombre" placeholder="Tu nombre" required>
            <input type="email" name="correo" placeholder="Tu correo electrónico" required>
            <input type="text" name="codigo" placeholder="Código promocional (opcional)">
            <input type="submit" value="Unirme ahora">
        </form>
        {% if mensaje %}
            <p class="{{ clase }}">{{ mensaje }}</p>
        {% endif %}
    </section>

    <section>
        <h2>📦 Planes disponibles</h2>
        <div class="plan">💥 Plan Mensual - {{ mensual }} COP</div>
        <div class="plan">🔥 Plan Trimestral - {{ trimestral }} COP</div>
        <div class="plan">💎 Plan Vitalicio - {{ vitalicio }} COP</div>
    </section>

    <div class="footer">
        &copy; 2025 Stark Goals. Todos los derechos reservados.
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    global usos_actuales

    # Precios normales
    precios = {
        "mensual": 30000,
        "trimestral": 70000,
        "vitalicio": 200000
    }

    mensaje = ""
    clase = ""

    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        codigo = request.form["codigo"].strip().upper()

        print(f"📬 Nuevo miembro: {nombre} - {correo} - Código: {codigo}")

        if codigo == DESCUENTO_CODIGO:
            if usos_actuales < USOS_DISPONIBLES:
                # Aplicar 20% de descuento
                for key in precios:
                    precios[key] = int(precios[key] * 0.8)
                usos_actuales += 1
                mensaje = f"✅ Código aplicado. ¡Tienes un 20% de descuento! ({USOS_DISPONIBLES - usos_actuales} disponibles)"
                clase = "descuento"
            else:
                mensaje = "❌ Código STARKBET agotado. Ya fue usado por 20 personas."
                clase = "error"
        elif codigo != "":
            mensaje = "⚠️ Código inválido. Asegúrate de escribirlo correctamente."
            clase = "error"

    return render_template_string(HTML,
                                  mensual=precios["mensual"],
                                  trimestral=precios["trimestral"],
                                  vitalicio=precios["vitalicio"],
                                  mensaje=mensaje,
                                  clase=clase)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
