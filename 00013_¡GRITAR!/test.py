
  def test_gritar_miguel_(self):
    self.assertEqual(gritar("miguel"), "¡MIGUEL!")

  def test_gritar_gritar_(self):
    self.assertEqual(gritar("gritar"), "¡GRITAR!")

  def test_gritar_minuto_(self):
    self.assertEqual(gritar("minuto"), "¡MINUTO!")


