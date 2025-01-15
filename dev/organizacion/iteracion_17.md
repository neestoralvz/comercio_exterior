# **Plan de Acción Final (Iteración 17)**

Tras la última revisión y la aplicación de cambios en la configuración del tema y en los archivos `.rst`, el proyecto está **casi listo**. No obstante, persisten **referencias a etiquetas indefinidas** que generan advertencias en la compilación. A continuación, se detalla un plan de cierre para **resolver** estos problemas remanentes y **consolidar** la documentación de manera definitiva.

---

## **1. Diagnóstico Breve de Advertencias Restantes**

Se han identificado **19 _warnings_** principales asociados a referencias a etiquetas que **no existen** o que **no se han definido** correctamente. Algunos ejemplos:

- `costos_asociados`
- `permisos_especiales`
- `procedimientos_operativos`
- `seguimiento_monitoreo`
- `planificacion_transporte`
- `planes_emergencia`
- `inspecciones_fronterizas`
- `tramites_aduanales`

Estas etiquetas se referencian mediante sintaxis como `:ref:` o `:numref:` en varios archivos `.rst`, pero **no cuentan con una definición** en el lugar correspondiente.

---

## **2. Plan de Acción Inmediato**

### 2.1 Localizar y Definir Etiquetas Faltantes

1. **Búsqueda Global**  
   - Ejecutar un comando de búsqueda, por ejemplo:  
     ```bash
     grep -r ":ref:`costos_asociados`" source
     ```  
     para cada etiqueta faltante. De esta manera, se identifica en qué archivos `.rst` está referenciada.

2. **Crear o Ajustar las Definiciones**  
   - Si el contenido al que se hace referencia **existe**, definir la etiqueta en su encabezado o en la sección adecuada, por ejemplo:  
     ```rst
     .. _costos_asociados:
     
     ============
     Costos Asociados
     ============
     ```
   - Si se considera que la sección no es necesaria o es un duplicado, **eliminar** la referencia o reemplazarla por otra etiqueta que sí exista.

3. **Compilar y Verificar**  
   - Tras cada ajuste, ejecutar `make html` y comprobar que el _warning_ desaparezca para cada etiqueta corregida.

### 2.2 Revisar la Lógica de Referencias Cruzadas

1. **Homogeneizar la Nomenclatura**  
   - Usar nombres de etiquetas **coherentes** y en **minúsculas** (por ejemplo, `.. _planificacion_transporte:`).  
   - Verificar que el título o sección donde se ubica la etiqueta coincida con su contenido (por ejemplo, “Planificación de Transporte” → `_planificacion_transporte`).

2. **Eliminar Referencias Obsoletas**  
   - Si se encuentra que algún archivo hace referencia a un concepto ya removido (por ejemplo, `planes_emergencia` que no existe en la versión actual), se debe **borrar** esa referencia o sustituirla por otra sección equivalente.

### 2.3 Revisión Final del Tema y Opciones

1. **Confirmar la Configuración**  
   - Revisar el `conf.py` para confirmar que no queden opciones obsoletas o innecesarias.  
   - Ajustar en `html_theme_options` únicamente las opciones **soportadas** por `sphinx-book-theme`.

2. **Probar Varias Plataformas**  
   - Visualizar la documentación generada en desktop y móvil, probando varios navegadores.  
   - Asegurarse de que el menú lateral, la búsqueda y los enlaces funcionen correctamente.

---

## **3. Validación y Cierre del Proyecto**

### 3.1 Compilación Limpia

- **Objetivo**: Alcanzar **cero _warnings_** de referencias indefinidas y configuraciones obsoletas.  
- **Acción**: Realizar una última corrida de `make html` o `sphinx-build` y revisar que no aparezcan advertencias en la terminal.

### 3.2 Retroalimentación de Interesados

- **Invitar a usuarios y revisores** a navegar por la documentación.  
- **Recopilar comentarios** sobre usabilidad, claridad y estructura.  
- **Registrar sugerencias** para futuras mejoras.

### 3.3 Publicación y Versión Definitiva

- **Asignar Versión**: Por ejemplo, “v1.0.0” para la versión liberada del proyecto.  
- **Actualizar el Historial de Cambios** (si aplica) con la fecha y la versión final.  
- **Publicar** la documentación en el entorno elegido (hosting interno, GitHub Pages, servidor propio, etc.).

### 3.4 Mantenimiento Futuro

- **Documentar el Proceso**: Dejar claro cómo se añaden nuevas secciones, cómo se definen etiquetas y cómo se compila.  
- **Programar Revisiones**: Establecer una periodicidad (trimestral, semestral) para mantener la documentación al día.  
- **Control de Versiones**: Continuar usando Git para rastrear cambios y fusionar aportaciones del equipo.

---

## **4. Conclusiones**

Con estas acciones finales, se resolverán los **warnings** restantes y la documentación **quedará libre de errores**, con un tema moderno y una estructura clara. Siguiendo los pasos propuestos, el equipo:

1. **Definirá** (o eliminará) etiquetas faltantes para un mapeo coherente de las referencias.  
2. **Verificará** la consistencia visual y funcional del tema “sphinx-book-theme”.  
3. **Logrará** la **versión final** de la documentación, lista para consulta y mantenimiento continuo.

De esta manera, el proyecto de documentación alcanzará un **estado óptimo**, brindando **claridad** y **utilidad** a todos los usuarios que requieran conocer los procesos, requerimientos y buenas prácticas en materia de comercio exterior. ¡Enhorabuena por el gran avance logrado!