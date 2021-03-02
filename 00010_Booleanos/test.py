
  def test_esta_entre_0_1_10_es_False(self):
    self.assertFalse(esta_entre(10, 1, 10))

  def test_esta_entre_4_4_9_es_False(self):
    self.assertFalse(esta_entre(4, 4, 9))

  def test_esta_entre_2_1_10_es_False(self):
    self.assertFalse(esta_entre(12, 1, 10))

  def test_esta_entre2_0_54_112_es_False(self):
    self.assertFalse(esta_entre(200, 54, 112))

  def test_esta_entre_7_0_100_es_True(self):
    self.assertTrue(esta_entre(67, 0, 100))

  def test_esta_entre_2_0_100_es_True(self):
    self.assertTrue(esta_entre(2, 0, 100))

  def test_esta_fuera_de_rango_0_1_10_es_False(self):
    self.assertFalse(esta_fuera_de_rango(10, 1, 10))

  def test_esta_fuera_de_rango_4_4_9_es_False(self):
    self.assertFalse(esta_fuera_de_rango(4, 4, 9))

  def test_esta_fuera_de_rango_2_1_10_es_True(self):
    self.assertTrue(esta_fuera_de_rango(12, 1, 10))

  def test_esta_fuera_de_rango2_0_54_112_es_True(self):
    self.assertTrue(esta_fuera_de_rango(200, 54, 112))

  def test_esta_fuera_de_rango_7_0_100_es_False(self):
    self.assertFalse(esta_fuera_de_rango(67, 0, 100))

  def test_esta_fuera_de_rango_2_0_100_es_False(self):
    self.assertFalse(esta_fuera_de_rango(2, 0, 100))


