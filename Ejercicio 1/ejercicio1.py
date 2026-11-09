def limpiar_registro_sensor(registro_raw: dict[str, str]):
    sensor_id = registro_raw.get("sensor_id", "").strip()

    temperatura = float(
        registro_raw.get("temperatura", "")
        .replace("°C", "")
        .replace("C", "")
        .strip()
    )

    ubicacion = registro_raw.get("ubicacion", "").strip()

    if ubicacion == "":
        ubicacion = "Ubicación desconocida"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]
        sensor_id = sensor["sensor_id"]

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor_id)

        suma_temperaturas += temperatura

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0

    return lista_sensores_alerta, promedio_temperatura


# Bloque principal

sensores_raw = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": " SENSOR-002 ",
        "temperatura": "35.8C",
        "ubicacion": "Planta Sur"
    },
    {
        "sensor_id": "SENSOR-003 ",
        "temperatura": "28.2C",
        "ubicacion": "Planta Este"
    },
    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "42.0C"
    },
    {
        "sensor_id": "SENSOR-005",
        "temperatura": "22.5C",
        "ubicacion": "Planta Oeste"
    }
]


# limpiar los registros

sensores_limpios = []

for registro in sensores_raw:
    registro_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(registro_limpio)

umbral = 30.0

sensores_alerta, promedio_global = generar_resumen_sensores(sensores_limpios, umbral)

for sensor in sensores_limpios:
    print(f"Sensor: {sensor['sensor_id']} - temperatura: {sensor['temperatura']} - ubicación: {sensor['ubicacion']}")

print(f"Umbral establecido: {umbral}")

print(f"Promedio global: {promedio_global:.2f} °C")

print(f"Dispositivos en alerta (superan el umbral): {sensores_alerta}")