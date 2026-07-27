#!/usr/bin/env python3
"""
Script para generar og-image.png para Hogar Integral
Crea una imagen 1200x630px optimizada para compartir en redes
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

def create_og_image(output_path="og-image.png"):
    """
    Crea la imagen Open Graph para Hogar Integral
    
    Dimensiones: 1200x630px (estándar para redes sociales)
    Colores: Verde Hogar Integral (#2C5F2D) y naranja (#E8A35D)
    """
    
    # Crear imagen con fondo gradiente simulado (dos colores)
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), color='#2C5F2D')
    draw = ImageDraw.Draw(img)
    
    # Dibujar gradiente simple (rectángulos superpuestos)
    for y in range(height):
        ratio = y / height
        # Interpolar entre verde oscuro y verde claro
        r = int(44 + (74 - 44) * ratio)
        g = int(95 + (143 - 95) * ratio)
        b = int(45 + (77 - 45) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Intentar cargar fuentes del sistema
    title_font = None
    subtitle_font = None
    emoji_font = None
    
    try:
        # En Windows
        title_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 100)
        subtitle_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 50)
    except:
        try:
            # En Mac
            title_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100)
            subtitle_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 50)
        except:
            try:
                # En Linux
                title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
                subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
            except:
                print("⚠️ No se encontraron fuentes TrueType, usando fuente por defecto")
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
    
    # Dibujar decoración izquierda (punto naranja)
    draw.ellipse([60, 100, 150, 190], fill='#E8A35D')
    
    # Dibujar decoración derecha (punto naranja)
    draw.ellipse([1050, 450, 1140, 540], fill='#E8A35D')
    
    # Dibujar título principal
    title = "Hogar Integral"
    try:
        draw.text((600, 200), title, fill='#FFFFFF', font=title_font, anchor='mm')
    except:
        draw.text((600, 200), title, fill='#FFFFFF', anchor='mm')
    
    # Dibujar subtítulo (principales características)
    subtitle = "Gestión Completa del Hogar"
    try:
        draw.text((600, 300), subtitle, fill='#E8A35D', font=subtitle_font, anchor='mm')
    except:
        draw.text((600, 300), subtitle, fill='#E8A35D', anchor='mm')
    
    # Dibujar características con iconos
    features = "📅 Calendario  •  💰 Gastos  •  🔧 Mantenimiento  •  📄 Documentos"
    try:
        draw.text((600, 420), features, fill='#FFFFFF', font=subtitle_font, anchor='mm')
    except:
        draw.text((600, 420), features, fill='#FFFFFF', anchor='mm')
    
    # Dibujar marca de agua
    watermark = "Funciona sin internet • Tus datos en tu dispositivo"
    try:
        watermark_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30) if title_font else ImageFont.load_default()
    except:
        watermark_font = ImageFont.load_default()
    
    try:
        draw.text((600, 570), watermark, fill=('rgba(255,255,255,0.7)'), font=watermark_font, anchor='mm')
    except:
        draw.text((600, 570), watermark, fill='#CCCCCC', anchor='mm')
    
    # Guardar imagen
    img.save(output_path, quality=95)
    
    return output_path

def main():
    """Función principal"""
    
    print("🎨 Generando imagen Open Graph para Hogar Integral...")
    print("─" * 50)
    
    try:
        from PIL import Image
        print("✅ PIL/Pillow detectado")
    except ImportError:
        print("❌ Error: Pillow no está instalado")
        print("\n📥 Instala con:")
        print("   pip install Pillow")
        sys.exit(1)
    
    try:
        output = create_og_image("og-image.png")
        print(f"✅ Imagen creada exitosamente: {output}")
        print(f"   Dimensiones: 1200x630px")
        print(f"   Formato: PNG (optimizado para redes sociales)")
        print("\n💡 Coloca este archivo en la carpeta raíz de tu proyecto:")
        print("   hogar-integral/")
        print("   ├── index.html")
        print("   ├── manifest.json")
        print("   ├── og-image.png  ← NUEVO")
        print("   └── README.md")
        print("\n✅ Lista para subir a GitHub Pages!")
        
    except Exception as e:
        print(f"❌ Error al crear la imagen: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
