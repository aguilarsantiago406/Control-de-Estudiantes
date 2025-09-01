# 📚 Sistema de Control de Estudiantes

Aplicación web desarrollada en **Django** que permite gestionar información de estudiantes de manera eficiente.  
Proporciona funcionalidades **CRUD** (Crear, Leer, Actualizar, Eliminar) para administrar datos como **nombre, carrera, ciclo y correo electrónico**.  

La interfaz está construida con **Bootstrap 5**, ofreciendo un diseño moderno, responsive e intuitivo para una mejor experiencia de usuario.

---

## 👥 Integrantes y Roles
- **Santiago Aguilar** - Scrum Master  
- **Angel Valencia** - Product Owner  
- **Franco Flores** - Developer  
- **Gonzalo Yermin** - Developer  
- **Piero Meza** - Developer  

---

## ⚙️ Instalación

### 🔑 Prerrequisitos
- [Python 3.8+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/) (gestor de paquetes de Python)  
- [virtualenv](https://virtualenv.pypa.io/) (recomendado)  

### 🚀 Pasos de instalación
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/aguilarsantiago406/Control-de-Estudiantes.git
   cd Control-de-estudiantes
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # En Windows
   source venv/bin/activate  # En Linux/Mac
   ```

3. **Configurar la base de datos**
   ```bash
   python manage.py migrate
   ```

4. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

5. **Acceder a la aplicación**
   👉 [http://localhost:8000](http://localhost:8000)

---

## 📝 Historias de Usuario

### 1️⃣ Gestión de Estudiantes
**Como** administrador académico  
**Quiero** poder ver la lista completa de estudiantes  
**Para** tener una visión general de todos los registros  

✅ **Criterios de aceptación**  
- Lista con ID, nombre, carrera, ciclo y correo  
- Opciones para ver detalles, editar y eliminar  
- Mensaje cuando no hay estudiantes registrados  

---

### 2️⃣ Registro de Nuevos Estudiantes
**Como** administrador académico  
**Quiero** poder agregar nuevos estudiantes al sistema  
**Para** mantener actualizada la base de datos  

✅ **Criterios de aceptación**  
- Formulario con validación de campos obligatorios  
- Mensajes de confirmación después de guardar  
- Redirección a la lista tras registro exitoso  

---

### 3️⃣ Visualización de Detalles
**Como** administrador académico  
**Quiero** ver la información detallada de un estudiante  
**Para** consultar todos sus datos en un solo lugar  

✅ **Criterios de aceptación**  
- Página con todos los campos del estudiante  
- Enlace funcional para el correo electrónico  
- Botones para editar o volver a la lista  

---

### 4️⃣ Edición de Información
**Como** administrador académico  
**Quiero** modificar la información de un estudiante existente  
**Para** corregir errores o actualizar datos  

✅ **Criterios de aceptación**  
- Formulario pre-llenado con datos actuales  
- Validación de campos  
- Mensaje de confirmación después de guardar  

---

### 5️⃣ Eliminación de Estudiantes
**Como** administrador académico  
**Quiero** eliminar estudiantes del sistema  
**Para** mantener la base de datos libre de registros obsoletos  

✅ **Criterios de aceptación**  
- Confirmación antes de eliminar  
- Mensaje de éxito después de la eliminación  
- Redirección a la lista principal  

---

### 6️⃣ Experiencia Responsive
**Como** usuario móvil  
**Quiero** que la aplicación se adapte a diferentes tamaños de pantalla  
**Para** poder usarla desde cualquier dispositivo  

✅ **Criterios de aceptación**  
- Diseño adaptable (desktop, tablet y móvil)  
- Interacciones accesibles en dispositivos táctiles  
- Texto legible en todos los dispositivos  

---

### 7️⃣ Navegación Intuitiva
**Como** usuario  
**Quiero** una interfaz clara y fácil de navegar  
**Para** encontrar rápidamente las funcionalidades que necesito  

✅ **Criterios de aceptación**  
- Menú de navegación coherente en todas las páginas  
- Botones con íconos descriptivos  
- Feedback visual en las interacciones  

---

## 📌 Tecnologías Utilizadas
- Django  
- Python  
- Bootstrap 5  
- SQLite 

---
