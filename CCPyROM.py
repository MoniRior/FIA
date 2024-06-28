import tkinter as tk
from tkinter import messagebox

def pertenencia_vibracion(x):
    if 0 <= x <= 3:
        return 'baja'
    elif 3 < x <= 7:
        return 'media'
    elif 7 < x <= 10:
        return 'alta'

def pertenencia_temperatura(x):
    if 0 <= x <= 20:
        return 'baja'
    elif 20 < x <= 60:
        return 'normal'
    elif 60 < x <= 100:
        return 'alta'

def pertenencia_presion(x):
    if 0 <= x <= 1:
        return 'baja'
    elif 1 < x <= 3:
        return 'normal'
    elif 3 < x <= 5:
        return 'alta'

def pertenencia_trabajadores(x):
    if 0 <= x <= 30:
        return 'bajo'
    elif 30 < x <= 70:
        return 'medio'
    elif 70 < x <= 100:
        return 'alto'

def diagnostico(vib, temp, pres, trab):
    reglas_diagnostico = {
        ('alta', 'alta', 'alta', 'bajo'): 'Alto riesgo de fallo, parar maquina y realizar mantenimiento inmediato',
        ('alta', 'alta', 'alta', 'medio'): 'Alto riesgo de fallo, parar maquina y realizar mantenimiento inmediato',
        ('alta', 'alta', 'alta', 'alto'): 'Alto riesgo de fallo, parar maquina y realizar mantenimiento inmediato',
        ('alta', 'alta', 'normal', 'bajo'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'alta', 'normal', 'medio'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'alta', 'normal', 'alto'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'alta', 'baja', 'bajo'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'alta', 'baja', 'medio'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'alta', 'baja', 'alto'): 'Desbalance significativo, realizar mantenimiento',
        # (Agrega aquí el resto de las reglas)
        ('alta', 'normal', 'alta', 'bajo'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'normal', 'alta', 'medio'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'normal', 'alta', 'alto'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'normal', 'normal', 'bajo'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'normal', 'normal', 'medio'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'normal', 'normal', 'alto'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'normal', 'baja', 'bajo'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'normal', 'baja', 'medio'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'normal', 'baja', 'alto'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'alta', 'bajo'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'baja', 'alta', 'medio'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'baja', 'alta', 'alto'): 'Desbalance significativo y revisar sistema de presión',
        ('alta', 'baja', 'normal', 'bajo'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'normal', 'medio'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'normal', 'alto'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'baja', 'bajo'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'baja', 'medio'): 'Desbalance significativo, realizar mantenimiento',
        ('alta', 'baja', 'baja', 'alto'): 'Desbalance significativo, realizar mantenimiento',
        ('media', 'alta', 'alta', 'bajo'): 'Revisar sistemas de refrigeración, desbalance y presión',
        ('media', 'alta', 'alta', 'medio'): 'Revisar sistemas de refrigeración, desbalance y presión',
        ('media', 'alta', 'alta', 'alto'): 'Revisar sistemas de refrigeración, desbalance y presión',
        ('media', 'alta', 'normal', 'bajo'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'alta', 'normal', 'medio'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'alta', 'normal', 'alto'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'alta', 'baja', 'bajo'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'alta', 'baja', 'medio'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'alta', 'baja', 'alto'): 'Revisar sistema de refrigeración y desbalance',
        ('media', 'normal', 'alta', 'bajo'): 'Monitorizar y revisar sistema de presión',
        ('media', 'normal', 'alta', 'medio'): 'Monitorizar y revisar sistema de presión',
        ('media', 'normal', 'alta', 'alto'): 'Monitorizar y revisar sistema de presión',
        ('media', 'normal', 'normal', 'bajo'): 'Monitorizar para posibles fallos',
        ('media', 'normal', 'normal', 'medio'): 'Monitorizar para posibles fallos',
        ('media', 'normal', 'normal', 'alto'): 'Monitorizar para posibles fallos',
        ('media', 'normal', 'baja', 'bajo'): 'Monitorizar para posibles fallos',
        ('media', 'normal', 'baja', 'medio'): 'Monitorizar para posibles fallos',
        ('media', 'normal', 'baja', 'alto'): 'Monitorizar para posibles fallos',
        ('media', 'baja', 'alta', 'bajo'): 'Posible desbalance y revisar sistema de presión',
        ('media', 'baja', 'alta', 'medio'): 'Posible desbalance y revisar sistema de presión',
        ('media', 'baja', 'alta', 'alto'): 'Posible desbalance y revisar sistema de presión',
        ('media', 'baja', 'normal', 'bajo'): 'Posible desbalance en el equipo',
        ('media', 'baja', 'normal', 'medio'): 'Posible desbalance en el equipo',
        ('media', 'baja', 'normal', 'alto'): 'Posible desbalance en el equipo',
        ('media', 'baja', 'baja', 'bajo'): 'Posible desbalance en el equipo',
        ('media', 'baja', 'baja', 'medio'): 'Posible desbalance en el equipo',
        ('media', 'baja', 'baja', 'alto'): 'Posible desbalance en el equipo',
        ('baja', 'alta', 'alta', 'bajo'): 'Revisar sistemas de refrigeración y presión',
        ('baja', 'alta', 'alta', 'medio'): 'Revisar sistemas de refrigeración y presión',
        ('baja', 'alta', 'alta', 'alto'): 'Revisar sistemas de refrigeración y presión',
        ('baja', 'alta', 'normal', 'bajo'): 'Revisar sistema de refrigeración',
        ('baja', 'alta', 'normal', 'medio'): 'Revisar sistema de refrigeración',
        ('baja', 'alta', 'normal', 'alto'): 'Revisar sistema de refrigeración',
        ('baja', 'alta', 'baja', 'bajo'): 'Revisar sistema de refrigeración',
        ('baja', 'alta', 'baja', 'medio'): 'Revisar sistema de refrigeración',
        ('baja', 'alta', 'baja', 'alto'): 'Revisar sistema de refrigeración',
        ('baja', 'normal', 'alta', 'bajo'): 'Revisar sistema de presión',
        ('baja', 'normal', 'alta', 'medio'): 'Revisar sistema de presión',
        ('baja', 'normal', 'alta', 'alto'): 'Revisar sistema de presión',
        ('baja', 'normal', 'normal', 'bajo'): 'Sistema en condiciones óptimas',
        ('baja', 'normal', 'normal', 'medio'): 'Sistema en condiciones óptimas',
        ('baja', 'normal', 'normal', 'alto'): 'Sistema en condiciones óptimas',
        ('baja', 'normal', 'baja', 'bajo'): 'Sistema en condiciones óptimas',
        ('baja', 'normal', 'baja', 'medio'): 'Sistema en condiciones óptimas',
        ('baja', 'normal', 'baja', 'alto'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'alta', 'bajo'): 'Revisar sistema de presión',
        ('baja', 'baja', 'alta', 'medio'): 'Revisar sistema de presión',
        ('baja', 'baja', 'alta', 'alto'): 'Revisar sistema de presión',
        ('baja', 'baja', 'normal', 'bajo'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'normal', 'medio'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'normal', 'alto'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'baja', 'bajo'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'baja', 'medio'): 'Sistema en condiciones óptimas',
        ('baja', 'baja', 'baja', 'alto'): 'Sistema en condiciones óptimas',
    }
    return reglas_diagnostico.get((vib, temp, pres, trab), 'Condiciones no encontradas')

def eficiencia_trabajo(trab):
    reglas_eficiencia = {
        'bajo': 'Eficiencia baja, alto riesgo de errores y accidentes',
        'medio': 'Eficiencia media, monitorizar el desempeño',
        'alto': 'Eficiencia alta, riesgo mínimo'
    }
    return reglas_eficiencia.get(trab, 'Condiciones no encontradas')

def diagnosticar():
    try:
        vibracion = float(entry_vibracion.get())
        temperatura = float(entry_temperatura.get())
        presion = float(entry_presion.get())
        trabajadores = float(entry_trabajadores.get())

        vib_cat = pertenencia_vibracion(vibracion)
        temp_cat = pertenencia_temperatura(temperatura)
        pres_cat = pertenencia_presion(presion)
        trab_cat = pertenencia_trabajadores(trabajadores)

        diag = diagnostico(vib_cat, temp_cat, pres_cat, trab_cat)
        ef = eficiencia_trabajo(trab_cat)

        messagebox.showinfo("Diagnóstico", f"Diagnóstico: {diag}\nEficiencia: {ef}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Interfaz gráfica
root = tk.Tk()
root.title("Sistema de Diagnóstico Difuso")

tk.Label(root, text="Vibración (0-10):").grid(row=0)
tk.Label(root, text="Temperatura (0-100):").grid(row=1)
tk.Label(root, text="Presión (0-5):").grid(row=2)
tk.Label(root, text="Porcentaje de Trabajadores (0-100):").grid(row=3)

entry_vibracion = tk.Entry(root)
entry_temperatura = tk.Entry(root)
entry_presion = tk.Entry(root)
entry_trabajadores = tk.Entry(root)

entry_vibracion.grid(row=0, column=1)
entry_temperatura.grid(row=1, column=1)
entry_presion.grid(row=2, column=1)
entry_trabajadores.grid(row=3, column=1)

tk.Button(root, text='Diagnosticar', command=diagnosticar).grid(row=4, column=1, pady=4)

root.mainloop()
