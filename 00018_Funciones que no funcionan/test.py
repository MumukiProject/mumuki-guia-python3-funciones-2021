
  def test_mitad_de_2_es_1(self):
    self.assertEqual(mitad(2), 1)


  def test_mitad_de_20_es_10(self):
    self.assertEqual(mitad(20), 10)


  def test_mitad_de_10_es_5(self):
    self.assertEqual(mitad(10), 5)
    

  def test_suma_lontigudes_de_hola_y_mundo_es_9(self):
    self.assertEqual(suma_lontigudes(hola_y_mundo), 9)


  def test_suma_lontifudes_de_llueva_cafe_es_6(self):
    self.assertEqual(suma_lontigudes("llueva", "café"), 10)

