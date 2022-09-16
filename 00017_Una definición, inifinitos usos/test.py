class Test(unittest.TestCase):

  def test_Rosario_no_es_mas_largo_que_Bahia_Blanca(self):
    self.assertFalse(es_mas_largo_que("Rosario", "Bahía Blanca"))

  def test_Valle_de_Uco_es_mas_largo_que_La_Punta(self):
    self.assertTrue(es_mas_largo_que("Valle de Uco", "La Punta"))