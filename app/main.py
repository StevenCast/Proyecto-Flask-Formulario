from conBD import * #Importar la conexion BD
from flask import Flask, request, render_template
from datetime import date
from datetime import datetime
import re #importar re para eliminar caracteres especiales
import json

app = Flask(__name__)
#acceder a index.html desde la ruta raiz, nota app sabe donde buscar si ya tiene la ruta definida
@app.route('/form', methods=['POST', 'GET'])
def registrarSubmit():
    if request.method == "POST":

        #datos a almacenar 
        #literal 1
            #Arreglar el almacenamiento de la seleccion de las actividades de los tipos de practica 
            #Verificar que se puedan ingresar los datos correctamente en la tabla "informe_actividad"
        tipo_Practicas = request.form.get('Tipo_Practicas')
        practica = request.form['comunitarias'] 


    

        #literal 2
        info_personal = request.form['Nombres_y_Apellidos_Estudiante']
        cedula_est = request.form['Cedula_Estudiante']
        email_est = request.form['Email_Estudiante']
        tel_est = request.form['Telefono_Estudiante']
        cel_est = request.form['Celular_Estudiante']

        #literal 3
                     
            #TABLA EN PROCESO
        
        #literal 4
        razon_soc = request.form['Razon_social']
        ruc = request.form['RUC']
        dir_insti = request.form['Direccion_Institucion']
        ciudad_insti = request.form['Ciudad_Institucion']
        tel_insti = request.form['Telefono_Institucion']
        cel_insti = request.form['Celular_Institucion']
        email_insti = request.form['Email_Institucion']
        tipo_insti = request.form['Tipo_Institucion']
        campo_insti = request.form['Campo_Institucion']
        campo_especific = request.form['Campo_Especifico']
        cod_convenio = request.form['Codigo_Convenio']
        nom_convenio = request.form['Nombre_Convenio']


        #literal 5

        """
        resumen_act = request.form['Resumen_Actividades']
        contribucion_act = request.form['Contribucion_Actividades']
        resultado_act = request.form['Resultado_Actividades']
        asignaturas_act = request.form['Asignaturas_Actividades']
        """

        
        resumen_act = request.form.get('Resumen_Actividades')
        contribucion_act = request.form.get('Contribucion_Actividades')
        resultado_act = request.form.get('Resultado_Actividades')
        asignaturas_act = request.form.get('Asignaturas_Actividades')
        
        #literal 6
        fecha_inicio = request.form['Fecha_Inicio_Practicas']
        fecha_fin = request.form['Fecha_Fin_Practicas']
        horas_solicitadas = request.form['Horas_Solicitadas']

        #literal 7
        
            #no hay tabla aun TABLA EN PROCESO
        
        #llamar a la funcion de la conexion de la base de datos realizada en el archivo conBD
        conexion_mysql = conexion_bd()
        cursor = conexion_mysql.cursor()

        #obtener el id de formulario
        fecha = datetime.now()
        fecha = str(fecha)
        tabla_formulario = "INSERT INTO formulario (fecha_emision_formulario) VALUES ('"+fecha+"')"
        cursor.execute(tabla_formulario)
        conexion_mysql.commit()
    
        #Seleccionar el ultimo id del formulario
        get_last_id_form = "SELECT max(id_documento) as id_documento from formulario"
        cursor.execute(get_last_id_form)
        last_id = cursor.fetchall()
        last_id = str(last_id)
        ''.join(last_id)
        last_id = re.sub("[]/(,/)[]","", last_id)
       
        #tabla actividades_convalidacion
        tabla_act_conv = ('INSERT INTO actividades_convalidacion (id_doc_FK, detalle_actividad, tipo_actividad) VALUES (%s,%s,%s)') 
        val_act_conv = (last_id, tipo_Practicas, practica)
        cursor.execute(tabla_act_conv, val_act_conv)  
        conexion_mysql.commit()

        #tabla estudiante
        tabla_empresa_pract = ('INSERT INTO estudiante (id_doc_FK, id_cedula, nombre_ape_estudiante, correo_estudiante, telefono_estudiante, celular_estudiante) VALUES (%s,%s,%s,%s,%s,%s)') 
        val_empresa = (last_id, cedula_est, info_personal, email_est, tel_est, cel_est)
        cursor.execute(tabla_empresa_pract, val_empresa)
        conexion_mysql.commit()

        #tabla empresa_practicas
        tabla_estudiante = ('INSERT INTO empresa_practica (id_doc_FK, RUC, razon_social, direccion_institucion, ciudad_pais_institucion, telefono_institucion, celular_institucion, correo_institucion, tipo_institucion, campo_amplio_institucion, campo_especifico_institucion, codigo_convenio_proyecto, nombre_convenio_proyecto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)') 
        val_estudiante = (last_id, ruc, razon_soc, dir_insti, ciudad_insti, tel_insti,cel_insti, email_insti, tipo_insti, campo_insti, campo_especific, cod_convenio, nom_convenio )
        cursor.execute(tabla_estudiante,val_estudiante )
        conexion_mysql.commit()

        #tabla informacion_adicional
        tabla_info_adicional = ('INSERT INTO informacion_adicional (id_doc_FK, fecha_inicio, fecha_fin, horas_solicitadas) VALUES (%s,%s, %s, %s)') 
        val_info = (last_id, fecha_inicio, fecha_fin, horas_solicitadas)
        cursor.execute(tabla_info_adicional, val_info)
        conexion_mysql.commit()
        
        
        #tabla informe_actividad
        tabla_informe_actividad = ('INSERT INTO informe_actividad (id_doc_FK, resumen_actividad, actividad_egreso_carrera, aporte_actividad, asignaturas_utilidad_actidad) VALUES (%s,%s,%s,%s,%s)') 
        val_informe = (last_id, resumen_act, contribucion_act, resultado_act, asignaturas_act)
        cursor.execute(tabla_informe_actividad, val_informe)
        conexion_mysql.commit()
        



        conexion_mysql.commit() #Confirmar cambios a la base de datos 
        cursor.close() #Cerrando conexion SQL
        conexion_mysql.close() #Cerrando conexion a la BD
        msg = "Registro con exito"
        print(cursor.rowcount, 'registro insertado')
        print("1 registro insertado, id", cursor.lastrowid)

        return render_template('index.html', msg="Formulario enviado")

    else:
        return render_template('index.html', msg= "Metodo HTTP incorrecto")


   
if __name__ == '__main__':
    app.add_url_rule('/form', view_func = registrarSubmit)
    app.run(debug=True, port= 5000)
