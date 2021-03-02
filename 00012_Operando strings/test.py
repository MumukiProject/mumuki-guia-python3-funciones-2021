
  def test_longitud_nombre_completo_Cosme_Fulanito(self):
    self.assertEqual(longitud_nombre_completo("Cosme", "Fulanito"), 14)

  def test_longitud_nombre_completo_John_Snow(self):
    self.assertEqual(longitud_nombre_completo("John", "Snow"), 9)

  def test_longitud_nombre_completo_Juana_Azurduy(self):
    self.assertEqual(longitud_nombre_completo("Juana", "Azurduy"), 13)
    
  def test_no_falta_contemplar_el_espacio(self):
    resultado = False
    try:
      resultado = [
        longitud_nombre_completo("", ""),
        longitud_nombre_completo("abc", "d"),
      ] == [0, 4]
    except:
      pass
    if resultado:
      self.fail("¡Te falta contemplar el espacio!")
    
      
