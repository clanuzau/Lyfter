# Fundamentos de Internet

## 1. Del Cliente al Servidor

Cuando escribimos `www.youtube.com` en un navegador y presionamos **Enter**, ocurren varios procesos en pocos segundos. El navegador debe localizar el servidor de YouTube, establecer una comunicación segura, solicitar la información necesaria y finalmente mostrar la página y el video.

### a. ¿Qué hace el cliente (navegador)?

El **cliente** es el dispositivo y, específicamente, el navegador que utilizamos, por ejemplo Chrome, Edge, Firefox o Safari.

Cuando escribimos:

`www.youtube.com`

el navegador interpreta que queremos acceder al sitio web de YouTube. Sin embargo, las computadoras en Internet se comunican principalmente mediante **direcciones IP**, por lo que el navegador necesita averiguar qué dirección IP corresponde al nombre `www.youtube.com`.

### b. ¿Qué papel cumple el DNS?

El **DNS (Domain Name System o Sistema de Nombres de Dominio)** funciona como una agenda de Internet.

Su función es convertir un nombre fácil de recordar, como:

`www.youtube.com`

en una dirección IP que pueda utilizar la computadora para localizar el servidor correspondiente.

De forma simplificada:

`www.youtube.com → DNS → dirección IP del servidor`

El navegador puede revisar primero si ya conoce esa dirección mediante información almacenada en caché. Si no la conoce, solicita la información a un servidor DNS.

### c. ¿Qué ocurre con la dirección IP?

Una vez que el navegador obtiene la **dirección IP**, ya sabe hacia qué servidor debe enviar la solicitud.

La dirección IP puede compararse con la dirección de una casa, pero dentro de Internet. La solicitud viaja por diferentes dispositivos de red, como routers, hasta llegar a la infraestructura del servicio solicitado.

En plataformas grandes como YouTube, un mismo dominio puede utilizar varias direcciones IP y múltiples servidores distribuidos geográficamente.

### d. ¿Qué hace el servidor?

Cuando el servidor recibe la solicitud del navegador, la procesa y determina qué información debe devolver.

Por ejemplo:

- Estructura de la página.
- Imágenes y miniaturas.
- Archivos JavaScript.
- Información relacionada con los videos.
- Datos de la cuenta si el usuario inició sesión.
- Información necesaria para reproducir el video seleccionado.

Cuando seleccionamos un video, el navegador realiza nuevas solicitudes para recibir el contenido audiovisual. El video normalmente se transmite por partes, mediante un proceso conocido como **streaming**.

### e. ¿Cómo entra en juego HTTP/HTTPS?

**HTTP (HyperText Transfer Protocol)** es un protocolo utilizado para intercambiar información entre clientes y servidores en la Web.

Actualmente, sitios como YouTube utilizan principalmente **HTTPS (HyperText Transfer Protocol Secure)**.

HTTPS agrega seguridad mediante cifrado utilizando **TLS (Transport Layer Security)**. Antes de intercambiar información protegida, el navegador y el servidor establecen una conexión segura y el navegador verifica el certificado digital presentado por el sitio.

El proceso general puede representarse así:

```text
Usuario
   |
   v
Navegador / Cliente
   |
   | Consulta DNS
   v
Servidor DNS
   |
   | Devuelve dirección IP
   v
Navegador / Cliente
   |
   | Solicitud HTTPS
   v
Servidor de YouTube
   |
   | Respuesta
   v
Navegador
   |
   v
Video en pantalla
```

En resumen:

`Usuario → Navegador → DNS → Dirección IP → Servidor → HTTPS → Respuesta → Navegador → Video`

---

## 2. Frontend y Backend en acción

Supongamos que estamos desarrollando una aplicación web que permite a los pacientes reservar citas médicas por Internet, seleccionar un doctor, consultar horarios disponibles y confirmar sus citas.

### Frontend

El **frontend** es la parte visual de la aplicación y corresponde a todo aquello que el usuario puede ver y utilizar directamente desde el navegador.

En una aplicación médica incluiría:

- Pantalla de inicio de sesión.
- Formulario con los datos del paciente.
- Calendario de fechas y horarios disponibles.
- Lista de médicos y especialidades.
- Botones para reservar, modificar o cancelar una cita.
- Mensajes de confirmación.

Tres tecnologías posibles para frontend son:

- **HTML:** define la estructura de la página.
- **CSS:** define la presentación y apariencia visual.
- **JavaScript:** agrega interactividad y permite comunicarse con el servidor.

### Backend

El **backend** corresponde a la lógica que se ejecuta en el servidor. Procesa las solicitudes recibidas desde el frontend, aplica las reglas del sistema y se comunica con la base de datos.

Entre sus funciones estarían:

- Verificar las credenciales del paciente.
- Consultar médicos y horarios disponibles.
- Validar que un horario no esté reservado.
- Guardar una nueva cita.
- Modificar o cancelar una cita.
- Devolver al frontend el resultado de la operación.

Tres tecnologías posibles para backend son:

- **Python**, utilizando frameworks como Django, Flask o FastAPI.
- **Java**, utilizando por ejemplo Spring Boot.
- **Node.js**, para ejecutar JavaScript del lado del servidor.

### Comunicación entre Frontend y Backend

El frontend y el backend pueden comunicarse mediante una **API (Application Programming Interface)** utilizando el protocolo **HTTP o HTTPS**.

El proceso funciona mediante el modelo **request/response**:

1. El usuario realiza una acción en el frontend.
2. El frontend envía un **request HTTP** a un endpoint de la API.
3. El backend recibe y procesa la solicitud.
4. Si es necesario, consulta o modifica información en una base de datos.
5. El backend genera un **response HTTP**.
6. El frontend recibe la respuesta y actualiza lo que ve el usuario.

Ejemplo: al presionar **Agendar cita**, el frontend podría enviar una solicitud `POST` al backend con la información del médico, fecha y hora seleccionados.

```text
Frontend
   |
   | HTTP Request
   v
API / Backend
   |
   | Consulta / actualización
   v
Base de datos
   |
   | Resultado
   v
Backend
   |
   | HTTP Response
   v
Frontend
```

---

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
| REST        | JSON / XML             | Alta                   | Baja                          | Alta                              |
| SOAP        | XML                    | Baja                   | Alta                          | Media                             |
| GraphQL     | JSON                   | Muy alta               | Media-Alta                    | Alta                              |

### ¿Cuál es más apropiada para una startup moderna? ¿Por qué?

Para una startup moderna que desarrolla un sistema de reservas en línea, **REST** sería una opción muy apropiada.

REST ofrece un buen equilibrio entre facilidad de desarrollo, compatibilidad, mantenimiento y escalabilidad. Utiliza HTTP/HTTPS de forma natural y normalmente intercambia información en formato JSON, lo que facilita la comunicación entre frontend y backend.

Además:

- Es relativamente sencilla de aprender e implementar.
- Tiene una gran cantidad de documentación y herramientas.
- Funciona bien con aplicaciones web y móviles.
- Facilita las operaciones CRUD: crear, consultar, actualizar y eliminar información.
- Puede integrarse fácilmente con servicios externos.

Ejemplos:

- `GET /reservas` → consultar reservas.
- `POST /reservas` → crear una reserva.
- `PUT /reservas/123` → reemplazar o actualizar una reserva.
- `PATCH /reservas/123` → actualizar parcialmente una reserva.
- `DELETE /reservas/123` → eliminar una reserva.

---

## 4. Explorando APIs con Postman

### 4.1 Selección de la API

- **Nombre de la API:** RESTful API - restful-api.dev
- **Descripción:** API REST pública utilizada para practicar operaciones HTTP sobre objetos. Permite consultar, crear y modificar recursos utilizando métodos como `GET`, `POST`, `PUT` y `PATCH`. Los datos se intercambian principalmente en formato JSON y puede utilizarse desde Postman para estudiar el funcionamiento de requests, responses, endpoints, headers, bodies y códigos de estado HTTP.

**Endpoint base utilizado:**

`https://api.restful-api.dev/objects`

### 4.2 Configuración en Postman

- **Nombre de la colección:** `PokeAPI_Mobile.postman_collection.json`
- **Solicitudes agregadas:**
  - **GET** - Consultar objetos.
  - **POST** - Crear un nuevo objeto.
  - **PUT** - Actualizar o reemplazar los datos de un objeto existente.
  - **PATCH** - Actualizar parcialmente un objeto existente.

> Nota: aunque el nombre de la colección contiene `PokeAPI`, las solicitudes indicadas en la práctica utilizan el endpoint `https://api.restful-api.dev/objects`.

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint | Código de estado | Notas |
|-----------|--------|----------|-------------------|-------|
| Consultar objetos | GET | `https://api.restful-api.dev/objects` | 200 OK | Devuelve una lista de objetos en formato JSON. |
| Crear objeto | POST | `https://api.restful-api.dev/objects` | 200 OK | Crea un nuevo recurso utilizando los datos enviados en el body. |
| Actualizar objeto | PUT | `https://api.restful-api.dev/objects/{id}` | 200 OK | Actualiza o reemplaza la información del objeto identificado por `{id}`. |
| Actualización parcial | PATCH | `https://api.restful-api.dev/objects/{id}` | 200 OK | Modifica solamente los campos indicados en el body. |

> Los códigos anteriores corresponden al comportamiento esperado de las operaciones ejecutadas correctamente contra esta API. Para una entrega basada estrictamente en evidencias, deben coincidir con las respuestas guardadas en la carpeta `Answers - Execution and analysis`.

### 4.4 Explicación técnica

#### Consultar objetos

- **Método HTTP:** `GET`
- **Endpoint:** `https://api.restful-api.dev/objects`
- **Parámetros / body:** No requiere body para consultar la lista general de objetos.
- **Descripción de la respuesta:** El servidor devuelve una colección de objetos en formato JSON. Cada objeto puede incluir un identificador (`id`), un nombre (`name`) y una estructura `data` con información adicional.

El método `GET` se utiliza para **consultar información** y normalmente no modifica los datos almacenados en el servidor.

#### Crear objeto

- **Método HTTP:** `POST`
- **Endpoint:** `https://api.restful-api.dev/objects`
- **Parámetros / body:** Se envía un body en formato JSON con la información del nuevo objeto.
- **Descripción de la respuesta:** La API procesa el JSON recibido y devuelve la representación del recurso creado. La respuesta normalmente incluye un identificador generado por el servidor junto con los datos enviados.

Ejemplo conceptual de body:

```json
{
  "name": "Apple MacBook Pro",
  "data": {
    "year": 2026,
    "price": 2500
  }
}
```

El método `POST` se utiliza normalmente para **crear un nuevo recurso**.

#### Actualizar objeto

- **Método HTTP:** `PUT`
- **Endpoint:** `https://api.restful-api.dev/objects/{id}`
- **Parámetros / body:** El identificador del objeto se coloca en la URL y se envía un JSON con los datos actualizados.
- **Descripción de la respuesta:** El servidor localiza el recurso por su identificador y procesa los nuevos datos. La respuesta muestra el recurso después de la actualización.

El método `PUT` se utiliza normalmente cuando se desea **actualizar o reemplazar la representación de un recurso**.

#### Actualización parcial de objeto

- **Método HTTP:** `PATCH`
- **Endpoint:** `https://api.restful-api.dev/objects/{id}`
- **Parámetros / body:** Se indica el `id` del recurso y en el body se envían únicamente los campos que se desean modificar.
- **Descripción de la respuesta:** El servidor actualiza los campos especificados sin necesidad de enviar nuevamente toda la información del recurso.

Ejemplo conceptual:

```json
{
  "name": "Apple MacBook Pro Updated"
}
```

El método `PATCH` resulta útil cuando solamente necesitamos **modificar una parte específica del recurso**.

### ¿Qué aprendiste del proceso?

Durante esta práctica aprendí cómo utilizar Postman para enviar solicitudes a una API REST y analizar las respuestas recibidas.

También comprendí que cada método HTTP tiene un propósito:

- `GET` permite consultar información.
- `POST` permite crear recursos.
- `PUT` permite actualizar o reemplazar un recurso.
- `PATCH` permite modificar parcialmente un recurso.

Además, aprendí a identificar elementos importantes de una comunicación HTTP, como el **endpoint**, el **método HTTP**, el **body JSON**, los **headers**, el **código de estado** y el contenido de la **respuesta**.

La práctica también permitió observar directamente el modelo **request/response**: Postman actúa como cliente, envía una solicitud HTTP al servidor de la API y el servidor devuelve una respuesta con un código de estado y datos.

### 4.5 Reflexión final

Esta práctica me permitió comprender de una manera más clara cómo se comunican las aplicaciones a través de Internet.

Antes de utilizar Postman, conceptos como API, endpoint, request, response y métodos HTTP podían parecer principalmente teóricos. Al ejecutar las solicitudes pude observar cómo un cliente envía información a un servidor y cómo el servidor procesa la petición y devuelve una respuesta.

También comprendí la importancia de los códigos de estado HTTP y del formato JSON para determinar si una operación fue realizada correctamente y para interpretar la información recibida.

Postman facilita las pruebas de una API porque permite ejecutar diferentes métodos HTTP sin necesidad de desarrollar previamente una aplicación completa. Por esta razón, es una herramienta útil para aprender, desarrollar, probar y documentar servicios REST.

En conclusión, esta actividad permitió relacionar los conceptos de cliente, servidor, HTTP, APIs REST y formato JSON con un ejemplo práctico, ayudándome a comprender mejor cómo funcionan muchas de las aplicaciones web que utilizamos diariamente.
