#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Eren Sefer'

class Bruch(object):
    """
    Bruch ist eine mathematische Klasse welche verwendet werden kann um mit Bruechen zu rechnen.
    Alle wichtigen magicfunktions wurden ueberschrieben um eine bessere Integration in den Python Workflow zu garantieren
    Die einfachsten Befehle werden in den folgenden Beispielen erlaeutert.

    :param int zaehler: Die Zahl beim Bruch oben
    :param int nenner: Die Zahl beim Bruch unten
    :ivar int zaehler: Die Zahl beim Bruch oben
    :ivar int nenner: Die Zahl beim Bruch unten

    Die einfachsten Befehle werden in den folgenden Beispielen erlaeutert.

    - **Erstellen eines Bruches**
        * Einfache Methode einen Bruch zu erstellen
            :Beispiel:
            >>> foo = Bruch(3,1)

        * Alternativer Weg einen Bruch zu erstellen
            :Beispiel:
            >>> foo = Bruch(4,5)
            >>> bar = Bruch(foo)
    - **Addieren eines Bruches**
        * Addieren von Zwei Bruechen
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> result = foo + bar #-> 19 / 5

        * Eingebettes Addieren
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> bar += foo #-> 19 / 5

        * Addieren mit einem int
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> result = Bruch(3,1) + 1 #-> 4 / 1 oder 4

     - **Subtrahieren eines Bruches**
        * Subtrahieren eines Bruches von einem Bruch
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> result = foo - bar #-> -11 / 5

        * Eingebettetes Subtrahieren
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> bar -= foo #-> -11 / 5

        * Subtrahieren eines ints von einem Bruch
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> result = Bruch(3,1) - 1 #-> 4 / 1 oder 4

    - **Subtrahieren eines Bruches**
        * Dividieren eines Bruches durch einen Bruch
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> result = foo / bar

        * Eingebettetes Dividieren
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> bar /= foo

        * Dividieren eines ints durch einem Bruch
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> result =  1 / Bruch(3,1)

    - **Muliplizieren eines Bruches**
        * Multiplizieren von Zwei Bruechen
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> result = foo * bar

        * Eingebettes multiplizieren
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> bar = Bruch(4,5)
            >>> bar *= foo

        * Multiplizieren mit einem int
            :Beispiel:
            >>> foo = Bruch(3,1)
            >>> result = Bruch(3,1) * 1 

            Alle anderen Methoden werden hier Beschrieben:

    """

    def __iter__(self):
        """
        Macht dieses Objekt iterrierbar
        """
        return (self.zaehler,self.nenner).__iter__()

    def __init__(self,zaehler=1,nenner=1):
        """
        Der Konstruktor

        :raises: TypeError: Falscher Datentyp
        :raises: ZeroDivisionError: 0 wurde für den Nenner gewählt.
        :param zaehler: Die Zahl beim Bruch oben als int oder Bruch
        :param nenner: Die Zahl beim Bruch unten als int
        """
        if nenner==0:
            raise ZeroDivisionError

        if type(zaehler) is int and type(nenner) is int:
            self.zaehler = zaehler
            self.nenner = nenner
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
            return
        if type(zaehler) is not int or isinstance(zaehler,Bruch):
            raise TypeError('Wrong Datatype:'+type(zaehler).__name__+'! Pleas use int or Bruch instead')
        if type(nenner) is not int:
            raise TypeError('Wrong Datatype:'+type(nenner).__name__+'! Pleas use int instead')



    def __float__(self):
        """
        ueberschreibt float()

        :return: float
        """
        back = float(self.zaehler/self.nenner)
        return back

    def __int__(self):
        """
        ueberschreibt int()

        :return: int
        """
        back = int(self.__float__())
        return back

    def __complex__(self):
        """
        ueberschreibt complex()

        :return: complex
        """
        back = complex(self.__float__())
        return back

    def __invert__(self):
        """
        Einen Bruch invertieren

        :return: Bruch
        """
        back = Bruch(self.nenner,self.zaehler)
        return back

    def __repr__(self):
        """
        Die Representation eines Bruches in Form eines Strings

        :return str: Die Representation
        """

        if self.nenner<0:
            self.nenner*=-1
            self.zaehler*=-1

        if self.nenner==1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __pow__(self, power):
        """
        Potenzieren eines Bruches

        :raises: TypeError: Falscher Datentyp
        :param power: Der Exponent
        :return: Bruch
        """
        if type(power) is int:
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError('Wrong Datatype:'+type(power).__name__+'! Pleas use int instead')

    def __abs__(self):
        """
        Der Absolutwert eines Bruches

        :return: Bruch
        """
        back = Bruch(abs(self.zaehler),abs(self.nenner))
        return back

    def __neg__(self):
        """
        Das negativ eines Bruches

        :return: Bruch
        """
        back = Bruch(-self.zaehler,self.nenner)
        return back

    def __makeBruch(other):
        """
        Um sicher zu gehen das ein Bruch erstellt/verwendet wird

        :raises: TypeError: Falscher Datentyp
        :param other: Der Bruch oder die Zahl
        :return: Bruch
        """

        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b=Bruch(other,1)
            return b
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int or a Bruch')

    def __eq__(self, other):
        """
        Bruch ist gleich mit

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        if self.zaehler == other.zaehler and self.nenner == other.nenner:
            return True
        elif float(self)==float(other):
            return True
        else:
            return False

    def __ne__(self, other):
        """
        Bruch ist nicht gleich mit

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        if self.zaehler != other.zaehler or self.nenner != other.nenner:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        Bruch ist groeßer gleich als

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)

        if self.__float__() >= float(other):
            return True
        else:
            return False

    def __le__(self, other):
        """
        Bruch ist kleiner gleich als

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        if self.__float__() <= float(other):
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Bruch ist kleiner als

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        if self.__float__() < float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Bruch ist groeßer als

        :param other: anderer Bruch oder Zahl
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        if self.__float__() > float(other):
            return True
        else:
            return False

    def __add__(self, other):
        """
        Das addieren eines Bruches mit einem Bruch oder einer Zahl

        :raises: TypeError: Falscher Datentyp
        :param other: Ein Bruch oder eine Zahl
        :return: Bruch
        """
        if isinstance(other, Bruch):
            other = Bruch.__makeBruch(other)
            return Bruch(self.zaehler*other.nenner+self.nenner*other.zaehler, self.nenner * other.nenner)
        elif type(other) is int:
            return Bruch(self.zaehler + (other*self.nenner),self.nenner)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int or Bruch')


    def __radd__(self, other):
        """
        Das addieren einer Zahl mit einem Bruch

        :param other: eine Zahl
        :return: Bruch
        """
        return self.__add__(other)

    def __iadd__(self, other):
        """
        Das interne addieren eines Bruches

        :param other: Bruch oder Zahl
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self


    def __sub__(self, other):
        """
        Das subtrahieren eines Bruches mit einem Bruch oder einer Zahl

        :raises: TypeError: Falscher Datentyp
        :param other: Ein Bruch oder eine Zahl
        :return: Bruch
        """
        if isinstance(other, Bruch):
            other = Bruch.__makeBruch(other)
            return Bruch(self.zaehler*other.nenner-self.nenner*other.zaehler, self.nenner * other.nenner)
        elif type(other) is int:
            return Bruch(self.zaehler - (other*self.nenner),self.nenner)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int or Bruch')

    def __isub__(self, other):
        """
        Das interne subtrahieren eines Bruches

        :param other: Bruch oder Zahl
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self

    def __rsub__(self, other):
        """
        Das subtrahieren einer Zahl weniger eines Bruches

        :raises: TypeError: Falscher Datentyp
        :param other: eine Zahl
        :return: Bruch
        """
        if type(other) is int:
            return Bruch((other*self.nenner)-self.zaehler,self.nenner)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int')

    def __mul__(self, other):
        """
        Das multiplizieren eines Bruches mit einem Bruch oder einer Zahl

        :raises: TypeError: Falscher Datentyp
        :param other: Ein Bruch oder eine Zahl
        :return: Bruch
        """
        if isinstance(other, Bruch):
            other = Bruch.__makeBruch(other)
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        elif type(other) is int:
            return Bruch(self.zaehler * other, self.nenner)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int or Bruch')

    def __imul__(self, other):
        """
        Das interne multiplizieren eines Bruches

        :param other: Bruch oder Zahl
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self*other
        return self

    def __rmul__(self, other):
        """
        Das multiplizieren einer Zahl mit einem Bruch

        :param other: eine Zahl
        :return: Bruch
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Das dividieren eines Bruches mit einem Bruch oder einer Zahl

        :raises: TypeError: Falscher Datentyp
        :param other: Ein Bruch oder eine Zahl
        :return: Bruch
        """
        if isinstance(other, Bruch):
            other = Bruch.__makeBruch(other)
            return Bruch(self.zaehler * other.nenner, self.nenner * other.zaehler)
        elif type(other) is int:
            return Bruch(self.zaehler, self.nenner * other)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int or Bruch')

    def __itruediv__(self, other):
        """
        Das interne dividieren eines Bruches

        :param other: Bruch oder Zahl
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self

    def __rtruediv__(self, other):
        """
        Das dividieren einer Zahl durch einen Bruch

        :raises: TypeError: Falscher Datentyp
        :param other: eine Zahl
        :return: Bruch
        """
        if type(other) is int:
            return Bruch(other * self.nenner,1 * self.zaehler)
        else:
            raise TypeError('Wrong Datatype:'+type(other).__name__+'! Please use int')