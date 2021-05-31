'''
# Z. Renderowanie szablonów

Plik z kodem: `template-render.py`

Stwórz plik `template-render.py`. W środku napisz program, który będzie:

- wczytywał zawartość pliku podanego jako pierwszy argument na wierszu poleceń
- wczytywał drugi i kolejne argumenty z wiersza poleceń w formie 'key=value'
  jako klucze i wartości do słownika
- formatował wczytany plik za pomocą metody `str.format()` używając utworzonego
  słownika jako źródła argumentów: `template_text.format(**template_args)`

Stwórz funkcję `render_template(file_path, **template_args)`, która będzie
formatować ten szablon. Niech będzie ona kluczowym elementem tego programu.
'''
def render_template(file_path, **template_args):
   # print(template_args)
    with open(file_path,"r") as s:
        print(s.read().format(**template_args))

render_template("text.txt", username="test")