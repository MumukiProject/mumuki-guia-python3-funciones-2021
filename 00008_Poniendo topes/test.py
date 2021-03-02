
  def test_extraer_100_20_es_80(self):
    self.assertEqual(extraer(100, 20), 80)
  
  def test_extraer_100_10_es_90(self):
    self.assertEqual(extraer(100, 10), 90)
  
  def test_extraer_100_0_es_100(self):
    self.assertEqual(extraer(100, 0), 100)
  
  def test_extraer_100_100_es_0(self):
    self.assertEqual(extraer(100, 100), 0)
  
  def test_extraer_100_120_es_0(self):
    self.assertEqual(extraer(100, 120), 0)
  
  def test_extraer_100_220_es_0(self):
    self.assertEqual(extraer(100, 220), 0)

