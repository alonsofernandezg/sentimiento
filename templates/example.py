
from transformers import pipeline


text = '''Costa Rica posee una serie de características y condiciones especiales que han permitido que durante los últimos años inversores extranjeros pongan la mirada en el país para desarrollar grandes proyectos inmobiliarios, especialmente en la provincia de Guanacaste.

Sin embargo, la falta de agua para este tipo de proyectos es uno de los principales desafíos para su desarrollo, por lo que resulta necesario que el gobierno trace una hoja de ruta para encontrar una solución, de acuerdo con expertos del sector.

Lea más: Guanacaste es un destino caliente para los bienes raíces

“Un obstáculo al desarrollo que debe ser resuelto es la disponibilidad de agua potable en áreas aptas para desarrollo industrial o turístico. En Costa Rica se nos ha hecho creer que el agua escasea, nada más alejado de la realidad en un país bendecido con abundancia de agua; hace falta inversión en infraestructura y fortalecer la gestión del recurso, para lo cual se requiere una intervención ordenada, pero con mano firme de las instituciones que administran el recurso”, dijo Manuel Freer, CEO de Urban Partners.

En este sentido, la ausencia de planeamiento para atender la problemática del agua en Guanacaste es lo que preocupa a Allan Rodríguez, presidente de FCS Capital.

“Como país hay que primero resolver algunos cuellos de botella para ese crecimiento, que todavía no hay una dirección muy clara, debe haber soluciones para el problema del agua en Guanacaste, lo que necesitamos es que algún gobierno gire una directriz que se tiene un compromiso país para poder solucionar eso y darles agua a todos esos proyectos”, dijo Rodríguez.

Lea más: Guanacaste en la ruta directa hacia la reactivación económica

Y es que el recurso hídrico es lo primero que se debe planificar para garantizar la llegada de nuevos proyectos turísticos en una zona como la provincia de Guanacaste, de acuerdo con Jorge Jiménez, CEO de Stone Alliance.

“El gobierno tiene un norte con el Proyecto de Abastecimiento de Agua para la Cuenca Media del río Tempisque y Comunidades Costeras (Paacume), pero como desarrollador no sé si va o no va, no sé si creerle o no creerle, no sé si proyectarme o no proyectarme hacia las fechas que se tienen, porque se vuelve un tema de una necesidad”, dijo Jiménez.

Precisamente Paacume, financiado con $450 millones, que llevaría agua a comunidades guanacastecas, es cuestionado por el presidente Rodrigo Chaves, quien anunció un análisis a fondo de la propuesta.

Las diferencias de lo que se cobraría por metro cúbico de agua en las dos márgenes del río Tempisque es lo que preocupa a Chaves y lo que pone en suspenso la inversión que necesita Guanacaste para garantizar el suministro del líquido por los próximos 50 años.

Ante este panorama los expertos del sector inmobiliario y los desarrolladores de proyectos aseguran que los grandes desarrollos turísticos, especialmente en Guanacaste, tendrán dificultades para avanzar mientras el gobierno no resuelva el problema de ausencia de agua en zonas estratégicas del país.'''



summarizer = pipeline("summarization")
print(summarizer(text, max_length=130, min_length=30, do_sample=False))