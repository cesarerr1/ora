# Guía Completa de Markdown

Markdown es un lenguaje de marcado ligero que permite formatear texto de manera sencilla. A continuación, se describen todos los elementos disponibles en Markdown con ejemplos.

---

## 1. Encabezados
Los encabezados se crean con `#`, `##`, `###`, etc.

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5
###### Encabezado 6
```

### Resultado:
# Encabezado 1  
## Encabezado 2  
### Encabezado 3  
#### Encabezado 4  
##### Encabezado 5  
###### Encabezado 6  

---

## 2. Estilos de Texto
Se pueden aplicar diferentes estilos al texto.

```markdown
**Negrita**  
*Itálica*  
***Negrita e Itálica***  
~~Texto tachado~~
```

### Resultado:
**Negrita**  
*Itálica*  
***Negrita e Itálica***  
~~Texto tachado~~

---

## 3. Listas

### Listas No Ordenadas:
```markdown
- Elemento 1
- Elemento 2
  - Subelemento 2.1
  - Subelemento 2.2
- Elemento 3
```

### Resultado:
- Elemento 1
- Elemento 2
  - Subelemento 2.1
  - Subelemento 2.2
- Elemento 3

### Listas Ordenadas:
```markdown
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
```

### Resultado:
1. Primer elemento
2. Segundo elemento
3. Tercer elemento

---

## 4. Enlaces

```markdown
[Texto del enlace](https://www.ejemplo.com)
```

### Resultado:
[Texto del enlace](https://www.ejemplo.com)

---

## 5. Imágenes

```markdown
![Texto alternativo](https://via.placeholder.com/150)
```

### Resultado:
![Texto alternativo](https://via.placeholder.com/150)

---

## 6. Citas
Las citas se crean con `>`.

```markdown
> Esta es una cita en Markdown.
```

### Resultado:
> Esta es una cita en Markdown.

---

## 7. Código en línea y Bloques de Código

### Código en línea:
```markdown
Se puede usar `código en línea` dentro del texto.
```

### Resultado:
Se puede usar `código en línea` dentro del texto.

### Bloques de código:
```markdown
```
print("Hola, mundo!")
```
```

### Resultado:
```
print("Hola, mundo!")
```

---

## 8. Tablas

```markdown
| Nombre  | Edad | Ciudad      |
|---------|------|------------|
| Juan    | 25   | Madrid     |
| María   | 30   | Barcelona  |
```

### Resultado:
| Nombre  | Edad | Ciudad      |
|---------|------|------------|
| Juan    | 25   | Madrid     |
| María   | 30   | Barcelona  |

---

## 9. Separadores
Los separadores se crean con `---` o `***`.

```markdown
---
***
```

### Resultado:
---
***

---

## 10. Checklists (Listas de Tareas)

```markdown
- [x] Tarea completada
- [ ] Tarea pendiente
```

### Resultado:
- [x] Tarea completada
- [ ] Tarea pendiente

---

## 11. Emoji

```markdown
😀 😎 🚀
```

### Resultado:
😀 😎 🚀

---

## 12. Notas al Pie

```markdown
Este es un texto con una nota al pie[^1].

[^1]: Esta es la nota al pie.
```

### Resultado:
Este es un texto con una nota al pie[^1].

[^1]: Esta es la nota al pie.

---

## 13. Comentarios (No visibles en la salida Markdown)

```markdown
<!-- Este es un comentario en Markdown -->
```

Esto no se mostrará en la vista final del documento.

---

## 14. Texto en color (Sólo soportado en algunas implementaciones)

```markdown
<span style="color: red;">Texto en rojo</span>
```

### Resultado:
<span style="color: red;">Texto en rojo</span>

(Algunas plataformas no admiten esto)

---

## 15. HTML dentro de Markdown
En Markdown también puedes usar HTML.

```markdown
<b>Texto en negrita con HTML</b>
<i>Texto en itálica con HTML</i>
```

### Resultado:
<b>Texto en negrita con HTML</b>  
<i>Texto en itálica con HTML</i>

---

## Conclusión
Markdown es una herramienta poderosa y versátil para formatear texto de manera sencilla y eficiente. ¡Esperamos que esta guía te ayude a aprovechar todo su potencial! 🎯
