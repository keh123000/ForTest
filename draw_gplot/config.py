import os


class Config(object):
    pass


class DevConfig(Config):
    REDIS_DATABASE_URI = 'redis://:123456@192.168.0.178:16379/0'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@host:port/dbname"
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


IMG_MAPPING = {
    "AP": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAyCAIAAACFyIEHAAACpklEQVR4nN2azY1iMQzHw2iaQJqtAXGihqUCKuCOtGWsxJ0KqICpgROiBth92wVzMMpkEsd2HDsrzf/4yId/OPnn473Z4/EI30gv/zsAY43jWW+PA3qZDRhvKcnpsHHty5enlhM/Ki8eyejyoHLhaZoqtlTGPLpJb4hkxtNvXyZUBjy2RtxJ1cvjtKqoqfQ83uujDknDM2alB7VStfFkJKfDxoMNGHS7igaeEqb2U4+IZiVUIp4yXCeYEMLlfJ6u+1rjLBLDQ5PMF7vlapU9V+BldWmkQFJVeditJAqTPZeoFj07BFAq/Pwj+Y9RmPX2CM/ZgXE6bKDMcrWaL3ZllOnDWpBlnDkPWqjsrNZBWixGTLSDIoGESc4Cfqn9QCt2TxOmxQi8wEXPZjtG/uRZ/vxNV5B3fzmfs2Lpk6x7tgW5oM3P/Ey3+3S7CysTbhZRY3JKeDriJjuJDUKbT39L8zP/8UZUi16kNiK6DGqbhGemf8103SP+RiQqbTRL0XyxYx2JUKyO2iYKczpsyjwj+fnSTZErNEWE0KnMVmQXNHTETtf9K90uJCqlSr1VMdCFWm+PMeKsF3ruMfmJIiYVIcJnFdsi1vfw+YMXbXE/EL1oNB1son2xarvvVVD1q2k50txfS6gkfz9bRp6WqKcfXN5/hcZdwnS76yaVRIotArhufl5o3fiEiqcL67ZuHVClxw38/GNCpVAnTKDPpyOp+klA/P2BN5UVCUh0H+KEZEsCarivsqXygAmK+9F+KicSkPL+WkflSgLS38e3Iv37+6epfCsJqPd9iZxKzqMjAdm8n5NQCXl6YILt+1OaiuXpJAEZvw8mkAgeExKQy/t6lArlMSQBOX4fklGVPOYwYcD3O5Eq5fEgAY34HgmQgMePBDSCZ6Q+AKuFCC0xJgFYAAAAAElFTkSuQmCC",
        "url": ""
    },
    "Core router": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAABGCAIAAADpbuUaAAADiUlEQVR4nN2bQU4rMQyGQ9ULcIPuUaX3xALpcYRueoxeolIlLtFjdNMjgMQCgYTYcwOOUBaBNE1sx7E9ycz7xYJC6vgbO3Yymrk6nU7uf9estwMt1AFytTmsNoeWM14Nka5KhuN+bePHr2wgB42MnlkL2TLxxLRCyMaLKlEtbR1kX7ZEfNQ5c5zHq72EVRdFbLz4xXILaV/xmfp4fPG/FN0rQI4TLxcdCTRda/H0l2O1OYTgBH2+P1RZAFOXuyaL8taVqDf3t7nNKoGcMKTYVxo1np6eQrMByDmBFkJMn3zZJxiWUbEd0GlwIgxvsdy6y+xdLLdJ5DE7aeGpjeHN/e1qc/AeENNgPPGY5GPQYrn1PARSrnjGOfaPKnnUPKrH/TrYxDotnZl0uJi6SNciZFL9wOlzpxOzRIbHAvFi4xx+P/4MadUSi5BeGKrPfH30YmeMIXNCk3zT6LhfG/dJc2sml94Aki76tWFMrMWlS6wfSNs9qgle0MfjizLhfyCfXt/+/f0jM5H0BtkixDqksyhCZmsy5IIhoVXFMoOMhSUec1EI9je0KiDzjSs9ALNQRP18f7CtER1aCAcVLKrFq5zr6fXNufXs8rNE9Mba/4DfCr9ztu8aXUSytsbyOyR4luVv32XZG8ImT9faop8cU8CR2P0LZUhTSE3DLBb9cCJzeKeR3fvMFa8+IJJizuRUgeUYpzcoUZP6AqerJp5BtdsxqzKTV1D0vqu42PYV6DZVeJJ4gvdFxyMiKudD8/XdDhukT92hRRB+Pe9YRy1vYpyonGV1PmoxzY0ElVkyvLfz+DMf1fWjFVRE+Y6nMa2m2l9AMoOJTT8ErYbtFye6W6ffAIAO8W3aduZ43jRdZcEk1HFTEaae5X8dSf3UKEGAt3WT5vTOxxmUQnbvEErlhA6MZMw5IdTgLfcUEo+bBGdwsu4UEhch7AqNQXEMMA/Lp5A8kmOg5Xt1PoUQyvtKx8CCa6foCXfviqFy5jCRDM+LdWi2nbJKyom+nncueTCiihPzQOaToalYBpBBQ7cZWY54Qpc/kSXmDLIC1ic/CuksODG17EaB0GGPZw/H2UYxocO2dcmgaSl3Hr2DPlFO0G3q8ezJcWIOl1+ZmMT6pOPBfS9kzKjFjKt7+WVUqPzVJHyNqS9tbbHQvpDWklZcCG1eLRwUVV/kB3lJ1OmwzVvXUJCEPH/LJvwNkXxgKIwe+SYAAAAASUVORK5CYII=",
        "url": ""
    },
    "DC": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAzCAIAAABOlFKiAAACr0lEQVR4nN2asXFCMQyGDZcBKGGFdJkgG4QF0rMAd1khRRZIzwJhA2ruUpGOMndQULDBSyFO59iWLMnyy13+iuQZW9/7Zdn4vckwDOEfafrXAThrPJ7lajPCKJMR8i0m+Xh/7jpWXx7Kk35UvXgk2dWDqguPaqr4Ujnz2Ca9I5IbT3v5cqHy4XGsxY1UrTxI0hiHV02/c4mA+o9QCQD0Y6My7g9GqGDL1cZwg9T+VMeIo2fWU2GsWq8U/khuGAyMLfHPYkt5lHKjRDxy6xEjJsnjToAdY6jnmzaJu+6jq3eB88c2I0GqdNKKiarsj1flNfdWLRiUUQUe4fDYV9yemvpUn8xYkhqYU02Ty/J7yewMJMnGN1BVizjs235H6wnVb1LWKLvioCVxy8O7+XM9na+ns+Q7koETf/LPtkTgddwfQjJ/AGm2mAu7Li4yiUtUe0nPVOMiCahQr4VGVYNrr3XVxsf9IYYJVL2uGkUNxjColiOtLShuPfWaVO4La24Lqr7fuZ7OvFGxmPuK86pFFAZKtB81GBWXOK/fnlWYoPq9IKECjCToBMyAxCRYIvXvOb5USHYoKh4hBsp4ftAyqVTro1a/zncen9741rvtOmmDVI7nO0EP8/X5Ch8K51UM1W67LjaQe1WVwRaECcz5W5Eq9wfVjtRIAiLrG1jBX43bNC6+hgTLYQJfD6jswqv5JclGKZGLLSjpeW8cOpAgD5WEVSpfEpDi/Lpa/XIxSOYKxkt9Hs8YRSmh6kQCMj5fyKmqX5kt5j0SLJH9eYk2/S7fF1V7LQmo9fmPnErOYyMB+Tyfk1AJeVpggu/zYJ6qytNIAnJ+vs0gMTwuJKAu7x8UqSgeR5jQ9X2XhCrn8SUB9X1/J0aKeXqQgMZ4vwqokKcfTAghDGPp/uFlhFF+AILQ6Dm6rw04AAAAAElFTkSuQmCC",
        "url": ""
    },
    "Firewall": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABNCAIAAACZlfVXAAAD+klEQVR4nNVbsU4bQRAdopShoIntiCBFNCgSjSWnvi+g5Bco0/IJ+YX8gkt/wdV2lCaSRUGERKLYrpASpCiiIMWg8bK7szd7O3MHrzLLcrw3+2Znd2+9c39/D88ZL/omUIpnL+Bl3wS2ON/fpc+ffv4R/tXOU8gBpH765i3+OP31Az9IZPQsgKJO7Akoo1FDnwK8wEfRKKMfARLqLhIyuhaQS53AaehOQMLucoQyOqoDFPgS9hAbAfM60NozHsbzJQB8Pjrw2g0FaFEHgPF8GVJHmAhQsTsCqS8Y9mAhQNEzaeoITQG6dhdCR4C6ZwDg7OJa0r9UQJd2j6KoDmjN7uP5cvH7lptnXITD0nIEOs5UADi7uP58dKBQByzsngZGXbMOdB/4RIc2OXD591/WTOdCbndEY88HAXVd13Xt/S5sIUyPD8fzZZaM3EwVinxkobquq6oSEpoeHwLA6bfvAPD1w/tET24dFiKLOsLPAYw6yWiURDI4DcJMBYHdo4jnQNRRCUyPD8PEUPdMtDY3J7FcCcmwsDs3PqJZKHc0hISEnkmLfBAgz91yEHWhZ9LdtkmMGrhgZ01QaU661vItVFWV0WiU2z2KeA5ENWRlgkdIPfCEBwt50z9+bs3Y42REHeFXYmDC38JXipnqPtBrjKxGo6PR+HRFTly3aE92OV3in0JOXrf0A3t4Q6M7PiIBikUAtGfSbSW2LsaeZ07qBdcNcqajR3UgoaEkJbgTnpN64ckIA8/pJPgWSi8ociEJJ1IcDQeSnEac7+/SOTtbicPRyFIlX7EhVusNF2xqT+0HtEJO/0lO3UUiMbi03looUYYT7VG0oE5ADbNq4jau1huvhdCwJwaDrYJkiqTEWK036Z7snrgVtwbkTpEue85d7JaSNGitSaHMWhy6eEvZOqc9RAdBtCcu2cqAauBDDdsR0E1WO8948JcSnIzcKtZIfVZNRsOB/JmEj18u3R8jq1FuNSFfk+au8hsXPAmwSWy3OA1zmitSHNxByJiFyiUlEmNWTbJkUIkQbWhMqbuYVZOzi+vG6uuiQYDiaVzje9/cxFitN6PhIGWhzgIPBYlhVYmzqAt7RmEiwPo0DgBGwwGWEZNjFcXTuCjcCtjPuZCE+tXtTdgYFu9O704LA391exOyJ8946GgE5AdVSB0PHbAgpJdM5gLkmwGXOkKy2rMVkGt3+aV1gpUAYeBLqCNMBGQFvjV1RPbVY7wvNN57nehzc3eXfogKdUSbu9N054mTkRBQ7hkP7S9/J4YiKkCdOqL09npURihA0TMeFK7fh45yBdhRR6h9f8CVgQKMPONB+QsQKOPdqz3rwBNMvsHhvkGxxpP4HlkJ/gP1s8ToeVXB6QAAAABJRU5ErkJggg==",
        "url": ""
    },
    "GK": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAA2CAIAAAAAkPOiAAADLklEQVR4nN1aQW4qMQxNvzgA217iI6qP1C1HYNMjcAm6pJfoEdj0CGyRikBwCba9AX/hKg2O7diJZzrtW9GZxHkvdmzPdO6u12v41fjz3QQ6R98KF8vNYrnpc8W7LqK0UcPb65MXk+ClsFO3NApuUthnvFXrrFHY80FCsEq1KfxebQhKqSqFgxKGUNRZVpjKs0ZIP1sjsxoJ93p2XfX2wQ9uOlvxhxyZJDjCtA/r5I1nK3RlPp20TA8hfLy/6C0slpvck8Q5FORpAsnL+cW1uIXQROxDE7/xbJXvMSxA2knXbtxHAciTTZ33fDoZz1ZkdCGWb69PxSvkxAhuIRLp9o24G0rMp5Pt8VR05mK52R5P3BgZIMx0pFM4PD3NpxONM4UxHGA82Leyit76yjQaB26Pp/TPfGHSUallsFDMkJzfUgJF2bC5NoUa5IGXW0Y79fH+gnxbHZM5GamnqbOoGZYKgGNM3nKBm0IhB8qk87vKoqLEqN2QoC0YfZKbEqqrEp8Kd/vz47+/dSbyUuGirdoUgkOUQhkItwmjXV67NoDPOQQeXpyC4vTq4ZlLgZOcTjUnykvebn8OIakWmqMoZzlNqdBkDjjVsn197vF558210crxmt7dit3+DD9G6GpFRhXyRAqy7QZXQK4yPYjpgc+hSaSpypNFJQ5LEzK5iklndGCIfen9w3M6ghNZjBw5nca2WximbM0Fwam8y2FN59KKcNWUilhUhGFp4TG9pAGk8gBstbCKJNmQO83Juw2QmjSTywtyLiUnDBO7/Zlj+6nwclhbZw4HMsOvJ2CUbBCq+3I90GOxDAj14u6zmSZHtNWdVFOnpo+smzfCshsRevBqDtORgaNX33nDYv3obMkF+K2+yY0pOpJarS3mTrenJ46KUrlvxk5LA/GfmWo3DgSo8hEVn6uNPwI5ebqn+aEiSdps13Y5rN11pgZT+y5rcRYKz/heIqOG3CBcaTz8As9yLnVhwFloN170gbZatFC5HNYwMbJxSdfK+Kr8rs1KEYm8f3jOf+hNmZaurPgV3uCYRZF104vw+fqyuyahPdV18gVtaNDsXqK6Ujgc/AfmBglCog2WxwAAAABJRU5ErkJggg==",
        "url": ""
    },
    "HandSet": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAA+CAIAAAC+4EyEAAABt0lEQVR4nO3XPW7CMBQA4EeVG3So0iG5QlkICysS6sJQiROgnoBTMHAATsDGVom1C2FpOEI8JMqQM6TDSx+O47+YdECKJyvYH+/550UZVVUFfbSnXhQltFwfeoCi+dbBkkeUpyy+nHuAHNpjQZ3W2xCRvTUSTjbOzFPGiiyaTOn5cb+yhZbrw3G/iuZbPwxUozVcA8JOnjIAUHEqq4bwNNNkvSXlGhA2S06wJBDPoWXD3dZIZRlDQ66GaNfbg4xcfDnn153XHiRw9JMfBnnK+JF8hfCox4qMD6HNoYV9PLH8gMYVYUW2mI1VKeB8afoihA0tPgThz6SQJ326mI0B4Ov7BxSZWkXEc5pMrSISOD40dwhamUrTbKT2+fFu5FRvl8cq/gP0b1A0mSasTFh5FxSfNlQi3KwawvciHX+H0G6p0S3nQ7PnGpe2Xbn9MEhY+RY8d4OkHFoAoOeU2y/N1AWCv2pPm6CPyFzYKDQsbO4QcbhqVhXSaGneJZ3v2lBqB0gNxadNPxBa93Bias6WZI3cQlMudlfOsGs2Vn7dQfvDT9XoA4MVWfDyih0ksNlCZAnzXSB9+wWYND2fjwvfWgAAAABJRU5ErkJggg==",
        "url": ""
    },
    "PSE": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAzCAIAAABOlFKiAAAC5ElEQVR4nN2aPW5bMQzHlSBHSLYga4BsGYLeIBfw6KmHMJAjGOghPGXMBXwDo0M2A10NAx3snsEdmDIMRYqURD0D/U/Pz9THz6Qo+uldnE6n9B/p8twTCNZ0PLP5aoJRLiaIN0ry9vp96FhjeTSfjKMayGMG2AiqITxVSyWWKpinQALzFg0CkcJ4TBLTOIQqhqcKptykk6qXp4HEbN6D1M7jJ7l7eNltl9pHras2qsb6oJzB7h5e8GI2Xz093tNvnx7vZ/MVtdGGaCgpqv3TVrbQH7uhB7+vKvzT9oOFyD+ul+dcJHQCnjnY8VZIrJ0VTdvmW+62xOPMYJ3ZKW/O2lb1L/NU5WKWvkQb+pEla3G4n++/2nK6wOP0skiSmwXuLZ6JfeEJr0E6q4eqPqHDSzQ6ewbzSNt80z/OD/98e/6RUrq9udas84DWum6Ie+ciFMObzfALD6iKyrOU0VKMMRPGQwIXu+1S2E/3h6PWEkovbWC0EV3nh8H5aQbUkhonFm9MpqPMwURHeSYKzZ1uQcnxxlSgcqoqeDzKSUC77fLKbLw/HPuRUJ0wGgnKVY/uD8fCoppMJkxKyfYPCpA8vsIAa644mTwkoAoekElFxxZzGr1pFul+EtBnvVNICaDNeuHcppKvnDHTo9kD02d+A5WRNutFbla1+aL8W6RTOJBQX2tU4B/mJVBnScHsC9+Kov2r/+fySVP/wDW12awX5uofEWDsTun/KUOintF81bxTNQcYk/38QAw/6p/cV1VUUSQgez/drBcYaVQYdWiG1879N68mTZVhUtXzxDz8krKWUJqjQpaKqOrno2Ke0PIeiFGF+4Sq8Xk8y2z5zVy3N9fj3ILqOi9hVGWe3/s/VZ3XkoB6z3/MKgnl52kjAcWcz3moPDw9JKDI8+DOeOuHSeHn2wWkAk8ICWjI+wcilcgTSAIa+H4Io8p5wmHSBO8jIRXlGUECmuL9KkACnnEkoCl4ptRf+8xRs59WrJYAAAAASUVORK5CYII=",
        "url": ""
    },
    "Splitter": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAyCAIAAACFyIEHAAACtklEQVR4nN2aPW4CQQyFTZRL0ECfLmko0lOnywlyBKQcAYkjcIJ01PQUNNDRs4pElTOQwskw8ng9Ho9nI+UVEdrMjz/sebPs7Oh6vcI/0t1fB+Cs4Xhe3j4GmGU0QL0Rks36td1cbXn6ctIOqRWPprpaUDXhKVoqvlTOPOZF70XlxlNvXy5IDjy+RlxJVcvTaFcxU9l5bCQYqLKvgcrCE6IJ89ncuYWnl/HEERTFFzeePLx3p6WmlzBXnwp40okPu2McGduSkDw9P7IdvahUPPJkfcGxJEJHl0WV4XH52oq+jsoZJZ4aB0OxacE2ZHAvKp7HhSTEly4nTfkpwyBUlMc9J5iK0KAvY9lxlAHceBpV12b9irnKxmeGibv/8Mzmq/F0UtRfGUEoMLb80nH62ijjufHgJT1VHITwO5QtP3aQVMH3s3iH3REAutOS8oAaybZ7hInji8I+mx0cB0TxPKimVHKhKo0uJkFJPCh3Kv2SI0r3q7RNngflQmWwrzjo0J4lQWl5oA5J830rB5cbZHj22wV4WIUgPVUWBjQ8s/kK/8bXDVRYYAKn0sFk5esthQnSU2XtC9QOJuvGgyKhh/yw/4WSzZcoe0NQSgK/exq9H02RwvXK8kvF2heY0hI+878X2EQB5xBBZqpYNSQo/vxnv12EzMQXyYdYl3N3OXdF0cQ67I71MABwL3Qg2YhTBD1WgUhFuTIvFVb58zkSN4tHMqZPlCEn8s5W8LwqzUZsgKWLyqW6UhU/H5XvJNgiJFS+BUZkfH7dt1P1IQHAeDppSoIynm+TBZO9nYUGS4VV7XkJu/+yWbp8finHNGAESX6tEevpNaqBgXoelGBxelWSoJzPgwUkod5cSFBNzutZKpbHkQTV8P2QrB+4w8AA7+8EqpinBQlqiPeREAl52pGghuAZUt/StKkPwujcOQAAAABJRU5ErkJggg==",
        "url": ""
    },
    "Terminal": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAABDCAIAAACnakQaAAADgElEQVR4nO2av2uaQRjHn5T+AaUJmIpkSKdKK8UlFZwDSrFbS8jm0NklEMiSpVDI0rmDm2RuKAqZpWkWCbakUwMpYiJEyRACmezw2Cfn+773/rh77s6C3+l8xfM+PM/Xe+45F8bjMfz/euB6ATzSxahUGyzr0NSCclJVqo1Br5/KpPHlQX2Tb1WJpRiNtfU9AEAGBKhUGw4joxgNxCiVi53umf9d+5HR8kar2R70+v7n9sOiFQ1RZBInhtHCuOgNAeBJZpGeu4JhwKi+fwMArWab3iUAUUZh2La/UrlYKhdxLDOMOc8w7+IiiU338xcjnrCIMDg2ERZTNVUgDHrGBAybxUNkwf02Ktw47tf8CnuFOsGYMIzt84Yhw9jwRqB4DePs9MdrGMeHWJlhUCvZ7ZjzPGRel5KQhMr+VCZ98v1HohlmqKVAOZaUAWYKAwSSpJotDGXNMWZJc4xZ0hwDAABevnrBsg5NaWFga6fTPQvsHdqUIsbx4RYOqBZyC6MejePDLREGB65gdL3hDwsA2Cdh+KXyhMVJjrH94LqFYd43XBnGyPaXyqSpUWDHMMynP/EAPboePn60CP/CksqkkSSfW+X9UmDECOwAjK6HAGABhgEjsoVhASbaG+Gr9N+eyXTRG2JfCwy4PwIDGcKbebKrjEAZcr+0ayhbd2Azj2Li6f/9+nnf47i7ARAqYpGcPpXPrbaabQoaAPw5/RhBAAAyjMh0jw9DJHc3AVW9H2bQ6zNgxG85Jg3Ls+fSk4knJ0WM29G5+NbV5X7gDFMYCt3sRDAyYX+NLqZDorG0vIEDD88EQ/OiRBmGGoS03LX1PcIIySjkIZgJhvhXFmUlgvEDKGhpeQNJ7pMqaSbI9K35VXx5dbkv7i04OTHcjs5l6R5TSOK1OAuMGBaKPs2MOYPe1WQAGQbwhcUPAwBPc/nf3Q5wANDMwRgoEzAgZDOLArwRKEMwLBJ/rGJdYbIbRl+eqCa4iZ0RGM+OgUp2oew2xwIBUCr34hbCsvvpaDKoFWQFiCj1/+EqwxzUN1ey27LNmwCmHtYK4XOqY6DUqkCQ1CAeht1aga7Gw2sWXQyYPsfGqQJla/Iw1D9/EV8ax0CFhyWyEAxhiFM7smGg/DCRQUBlCztv373GMTHEL36ZMVCeKjDmgrKFndOjD2iGpNW7EQwUHoB0jhPxZRDDpv4CkASkjroWRVYAAAAASUVORK5CYII=",
        "url": ""
    },
    "TV": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADoAAABCCAIAAACJqFLTAAACwElEQVR4nO2av04bQRCHhygSTboUGCyZ+A1CE2hokejSpbHS+RGQ8giRUvAAdBYNXTokWlLYNBhFSut4Jft8hTuaVKYYMpzv9v/N3i6Cr1qf5dWn8e/2ZtfeWK1W8Hx4E1vADR/dz/0Ldg9LNpzCUBL9efaF28eAQ3WrRW2+zFbVNWo1VmaDrlP9SLrXH5yffa3lpUCp6/1Fv4N/NGaXlme3TijvYZPGvf7Aex4p5eoy3j0hyvyki6KL2aTV7rJMjfBKP4Zh/+gHDlrt7mI2WcwmNecleLPxWF3U3d7t0BtplnlNF0lZWqKLpCm9tpCJfC7yOY6zqfjYeY/jdAItWXePD/dwcHl9m00FjlvtLkrXkFzjHjZJutcfWErLHxPHh3sknU1FURoAIkrrOrImpWmsNzY3kCVpuh4lG7b9biLZcGjPUwi0815NI8212I1uhqObYfEKGXvuhMkYCoFmWexKosSHg28A8NZ7XjS+vL6F/8b4IKRsuD4IpaK/fv8pvvTXRVikbUSRurqIRlpvrPrqVXCe4qgCDYp1w9UVuKpLWGbDQxRh1kX02ZjOcu+Zg+giVWmRz3fbW3XmDH4CWQx0fZo4MGU0fgHnuxF51Q3Jq25Inrnu/qeDsVhGUbFhTbeztYODsVimJv13+B2q1S1uv9KRRldQtTjFNmoslnRY1jwkiuhuNap0rDKXXMFmZYiVjaorkO7o6kTzyXQC/VTd0dWJk3RYLwXlMOiNIXagJdk1lhniBVp5q6WZDcPKYC/dTJmtWpx0smHbkblmI5C0WwMZPdA+/W7EQPu3506Bdp08uzuVXq+1m3DKhj0qV3D9Y5aG6q/KVfCMTHOkpxFF2PZqxmzoye5Oja7Au7W0eXpLsRFF+A9M0dgmG+AiioQ63zVKu4oiYc8ZVNnwcwXGlUEPllnkc29RpCFdLh4ABTUsOIUlgZUAAAAASUVORK5CYII=",
        "url": ""
    },
    "WAP": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAAzCAIAAABKYYKfAAADOklEQVR4nN2aP05bQRDGh4grABIC15ElSyhF8AkoXaUjBfIdkHyESNwBpcAdFSUngBQRElKUOrJAFJzBKYZs1rOzs9/+e5HyVc9+9tv5vfl2Zt+frfV6Tf+d3v3rALpoOKrZfDnYWFsDOFDw3Fye9h6xO1UsRV3ZOlIlLdcPrAtV1hTqwdaYinnAQH34tmwta2BNlZvNlw2L5HaToyABjcYL8c3RdBIep0nSah2o8hiRgQmpZKuiQqr2aLz49eML+EfjOFkqpLLD8qOZzZcPd48hWPIg6tFAZVeLgml9NJ3M5stwXuEj5v4lo1pU1ihRG0bjRVgt7KHxpKEOrC+7IqbiAyJsaQe27SSsYjcSdjosB7r/I6cnixz3njGWEZVO1Tw5RgSxXbH1lPveYFOocCTfSFmnH0k+/yYZjMq2Hf4CF3eh8F8Nl6o3l6dIVGKp9VYD8a6qrhUKJAqGn+pY12Yhob7l6mX1RER7B/vJaLil2gMbcm3KcGzZEA93j257w4FZbHyy/YHV0y/caMDU+NZHIrVavKyeBJhaFXjD7TqaTpIFo8dtJp/n44f3vKFXdpE02y3GkFmnH2zNbsSQ59v3n/zR6sK4IRElF354bzB4Pn3+en11ll7dtmLzg1a7KiiB5HgY7/rqjPA1ezjZkhL2AzuPoViKRLoo60okN2lhZysGQ3hcqSCQ6v72/Pjkgrcrq39B+XZIIifCfn6u/l5fubhV+WBOYN44rFhLNbJnTyHVfjzKxlWjAXZ/e67+xgAruNfphFtO8LA2HMih20mjUkOCquRhRa/wBZvLlbqXJdjEKiYmsa7lDXAKxVyduG/hovep+MtYYsvyVjyFVCVqoDObiqcqt7M1sZwQeo8pZkgjbwibarkaHlbevVuV7fjkglOaVf0Ny8W6EH65VXJH2g/d8YS7fPlsPSwnVHif3Takqr2D/QF4WFXPRJKdTeh59UomA1K1ETV4goqzPa9ejSlE1SlyavNcGAE73N2hbpYTavm0O8nGuaKePKz2byYYbIe7O/VVG1Gvt0hUtrBaUGseVsd3Y0Iwf2pRHx5W9/eYfDbOFfXkYQ3xzhn9YWOq3kg0GNXA+g1lXaHLxN/OYAAAAABJRU5ErkJggg==",
        "url": ""
    },
    "OLT": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAABDCAIAAACnakQaAAADgElEQVR4nO2av2uaQRjHn5T+AaUJmIpkSKdKK8UlFZwDSrFbS8jm0NklEMiSpVDI0rmDm2RuKAqZpWkWCbakUwMpYiJEyRACmezw2Cfn+773/rh77s6C3+l8xfM+PM/Xe+45F8bjMfz/euB6ATzSxahUGyzr0NSCclJVqo1Br5/KpPHlQX2Tb1WJpRiNtfU9AEAGBKhUGw4joxgNxCiVi53umf9d+5HR8kar2R70+v7n9sOiFQ1RZBInhtHCuOgNAeBJZpGeu4JhwKi+fwMArWab3iUAUUZh2La/UrlYKhdxLDOMOc8w7+IiiU338xcjnrCIMDg2ERZTNVUgDHrGBAybxUNkwf02Ktw47tf8CnuFOsGYMIzt84Yhw9jwRqB4DePs9MdrGMeHWJlhUCvZ7ZjzPGRel5KQhMr+VCZ98v1HohlmqKVAOZaUAWYKAwSSpJotDGXNMWZJc4xZ0hwDAABevnrBsg5NaWFga6fTPQvsHdqUIsbx4RYOqBZyC6MejePDLREGB65gdL3hDwsA2Cdh+KXyhMVJjrH94LqFYd43XBnGyPaXyqSpUWDHMMynP/EAPboePn60CP/CksqkkSSfW+X9UmDECOwAjK6HAGABhgEjsoVhASbaG+Gr9N+eyXTRG2JfCwy4PwIDGcKbebKrjEAZcr+0ayhbd2Azj2Li6f/9+nnf47i7ARAqYpGcPpXPrbaabQoaAPw5/RhBAAAyjMh0jw9DJHc3AVW9H2bQ6zNgxG85Jg3Ls+fSk4knJ0WM29G5+NbV5X7gDFMYCt3sRDAyYX+NLqZDorG0vIEDD88EQ/OiRBmGGoS03LX1PcIIySjkIZgJhvhXFmUlgvEDKGhpeQNJ7pMqaSbI9K35VXx5dbkv7i04OTHcjs5l6R5TSOK1OAuMGBaKPs2MOYPe1WQAGQbwhcUPAwBPc/nf3Q5wANDMwRgoEzAgZDOLArwRKEMwLBJ/rGJdYbIbRl+eqCa4iZ0RGM+OgUp2oew2xwIBUCr34hbCsvvpaDKoFWQFiCj1/+EqwxzUN1ey27LNmwCmHtYK4XOqY6DUqkCQ1CAeht1aga7Gw2sWXQyYPsfGqQJla/Iw1D9/EV8ax0CFhyWyEAxhiFM7smGg/DCRQUBlCztv373GMTHEL36ZMVCeKjDmgrKFndOjD2iGpNW7EQwUHoB0jhPxZRDDpv4CkASkjroWRVYAAAAASUVORK5CYII=",
        "url": ""
    },
    "ODN": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADoAAABCCAIAAACJqFLTAAACwElEQVR4nO2av04bQRCHhygSTboUGCyZ+A1CE2hokejSpbHS+RGQ8giRUvAAdBYNXTokWlLYNBhFSut4Jft8hTuaVKYYMpzv9v/N3i6Cr1qf5dWn8e/2ZtfeWK1W8Hx4E1vADR/dz/0Ldg9LNpzCUBL9efaF28eAQ3WrRW2+zFbVNWo1VmaDrlP9SLrXH5yffa3lpUCp6/1Fv4N/NGaXlme3TijvYZPGvf7Aex4p5eoy3j0hyvyki6KL2aTV7rJMjfBKP4Zh/+gHDlrt7mI2WcwmNecleLPxWF3U3d7t0BtplnlNF0lZWqKLpCm9tpCJfC7yOY6zqfjYeY/jdAItWXePD/dwcHl9m00FjlvtLkrXkFzjHjZJutcfWErLHxPHh3sknU1FURoAIkrrOrImpWmsNzY3kCVpuh4lG7b9biLZcGjPUwi0815NI8212I1uhqObYfEKGXvuhMkYCoFmWexKosSHg28A8NZ7XjS+vL6F/8b4IKRsuD4IpaK/fv8pvvTXRVikbUSRurqIRlpvrPrqVXCe4qgCDYp1w9UVuKpLWGbDQxRh1kX02ZjOcu+Zg+giVWmRz3fbW3XmDH4CWQx0fZo4MGU0fgHnuxF51Q3Jq25Inrnu/qeDsVhGUbFhTbeztYODsVimJv13+B2q1S1uv9KRRldQtTjFNmoslnRY1jwkiuhuNap0rDKXXMFmZYiVjaorkO7o6kTzyXQC/VTd0dWJk3RYLwXlMOiNIXagJdk1lhniBVp5q6WZDcPKYC/dTJmtWpx0smHbkblmI5C0WwMZPdA+/W7EQPu3506Bdp08uzuVXq+1m3DKhj0qV3D9Y5aG6q/KVfCMTHOkpxFF2PZqxmzoye5Oja7Au7W0eXpLsRFF+A9M0dgmG+AiioQ63zVKu4oiYc8ZVNnwcwXGlUEPllnkc29RpCFdLh4ABTUsOIUlgZUAAAAASUVORK5CYII=",
        "url": ""
    },
    "ONT": {
        "b64code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAAzCAIAAABKYYKfAAADOklEQVR4nN2aP05bQRDGh4grABIC15ElSyhF8AkoXaUjBfIdkHyESNwBpcAdFSUngBQRElKUOrJAFJzBKYZs1rOzs9/+e5HyVc9+9tv5vfl2Zt+frfV6Tf+d3v3rALpoOKrZfDnYWFsDOFDw3Fye9h6xO1UsRV3ZOlIlLdcPrAtV1hTqwdaYinnAQH34tmwta2BNlZvNlw2L5HaToyABjcYL8c3RdBIep0nSah2o8hiRgQmpZKuiQqr2aLz49eML+EfjOFkqpLLD8qOZzZcPd48hWPIg6tFAZVeLgml9NJ3M5stwXuEj5v4lo1pU1ihRG0bjRVgt7KHxpKEOrC+7IqbiAyJsaQe27SSsYjcSdjosB7r/I6cnixz3njGWEZVO1Tw5RgSxXbH1lPveYFOocCTfSFmnH0k+/yYZjMq2Hf4CF3eh8F8Nl6o3l6dIVGKp9VYD8a6qrhUKJAqGn+pY12Yhob7l6mX1RER7B/vJaLil2gMbcm3KcGzZEA93j257w4FZbHyy/YHV0y/caMDU+NZHIrVavKyeBJhaFXjD7TqaTpIFo8dtJp/n44f3vKFXdpE02y3GkFmnH2zNbsSQ59v3n/zR6sK4IRElF354bzB4Pn3+en11ll7dtmLzg1a7KiiB5HgY7/rqjPA1ezjZkhL2AzuPoViKRLoo60okN2lhZysGQ3hcqSCQ6v72/Pjkgrcrq39B+XZIIifCfn6u/l5fubhV+WBOYN44rFhLNbJnTyHVfjzKxlWjAXZ/e67+xgAruNfphFtO8LA2HMih20mjUkOCquRhRa/wBZvLlbqXJdjEKiYmsa7lDXAKxVyduG/hovep+MtYYsvyVjyFVCVqoDObiqcqt7M1sZwQeo8pZkgjbwibarkaHlbevVuV7fjkglOaVf0Ny8W6EH65VXJH2g/d8YS7fPlsPSwnVHif3Takqr2D/QF4WFXPRJKdTeh59UomA1K1ETV4goqzPa9ejSlE1SlyavNcGAE73N2hbpYTavm0O8nGuaKePKz2byYYbIe7O/VVG1Gvt0hUtrBaUGseVsd3Y0Iwf2pRHx5W9/eYfDbOFfXkYQ3xzhn9YWOq3kg0GNXA+g1lXaHLxN/OYAAAAABJRU5ErkJggg==",
        "url": ""
    }
}

TEMP_GRAPH_BASE_IMG_PATH = '%s/data/graph/img/' % os.getcwd()
TEMP_GRAPH_BASE_PAGE_PATH = '%s/data/graph/page/' % os.getcwd()
