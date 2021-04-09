
  def test_esta_entre_10_1_10_es_False(self):
    self.assertFalse(esta_entre(10, 1, 10))

  def test_esta_entre_4_4_9_es_False(self):
    self.assertFalse(esta_entre(4, 4, 9))

  def test_esta_entre_12_1_10_es_False(self):
    self.assertFalse(esta_entre(12, 1, 10))

  def test_esta_entre_200_54_112_es_False(self):
    self.assertFalse(esta_entre(200, 54, 112))

  def test_esta_entre_67_0_100_es_True(self):
    self.assertTrue(esta_entre(67, 0, 100))

  def test_esta_entre_2_0_100_es_True(self):
    self.assertTrue(esta_entre(2, 0, 100))

  def test_esta_fuera_de_rango_0_1_10_es_False(self):
    self.assertTrue(esta_fuera_de_rango(0, 1, 10))

  def test_esta_fuera_de_rango_12_1_10_es_True(self):
    self.assertTrue(esta_fuera_de_rango(12, 1, 10))

  def test_esta_fuera_de_rango_200_54_112_es_True(self):
    self.assertTrue(esta_fuera_de_rango(200, 54, 112))

  def test_esta_fuera_de_rango_67_0_100_es_False(self):
    self.assertFalse(esta_fuera_de_rango(67, 0, 100))

  def test_esta_fuera_de_rango_2_0_100_es_False(self):
    self.assertFalse(esta_fuera_de_rango(2, 0, 100))


