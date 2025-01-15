.. _diagramas_proceso:


Diagramas       de              Proceso        
=============== =============== ===============
=============== =============== ===============

Este documento contiene los diagramas de flujo que ilustran los procesos
principales de exportación y ventas.


Diagrama de Proceso de Exportación
----------------------------------

.. mermaid::

   graph TD
      A[Inicio] --> B[Preparación Documental]
      B --> C[Documentos Comerciales]
      B --> D[Documentos Aduaneros]
      B --> E[Documentos Técnicos]

      C --> |Factura/Lista Empaque| F[Pre-validación Documental]
      D --> |Pedimento/DUCA| F
      E --> |MSDS/Permisos| F

      F --> G{Documentación Completa?}
      G --> |No| B
      G --> |Sí| H[Llegada a Frontera]

      H --> I[Registro en Aduana]
      I --> J[Módulo de Selección]

      J --> |Verde| L[Liberación Directa]
      J --> |Rojo| K[Revisión Física]
      K --> |Aprobado| L
      K --> |Rechazado| M[Correcciones]
      M --> H

      L --> N[Cruce Fronterizo]
      N --> O[Fin]


Diagrama de Proceso de Ventas
-----------------------------

.. mermaid::

   graph TD
      A[Inicio] --> B[Solicitud del Cliente]
      B --> C[Verificación Requisitos]

      C --> D{Cliente Calificado?}
      D --> |No| E[Proceso Calificación]
      D --> |Sí| F[Cotización]

      E --> |Aprobado| F
      E --> |Rechazado| Z[Fin]

      F --> G[Negociación]
      G --> H{Acuerdo?}
      H --> |No| Z
      H --> |Sí| I[Contrato]

      I --> J[Documentación Comercial]
      J --> K[Facturación]
      K --> L[Programación Logística]

      L --> M[Coordinación Transporte]
      M --> N[Entrega]
      N --> O[Confirmación]
      O --> P[Fin]


Historial de Cambios
--------------------


  * **2024-03-20:** Creación inicial de los diagramas de proceso.



  * **2024-03-21:** Ajustes en el flujo de exportación para incluir el módulo de selección.