import logging
log = logging.getLogger('pompa.report')


def generate_report(self, mode):
        """ Returns report content in string
        """
        report = ""
        # TODO:
        # Report making processes
        if mode == 'checking':
            report = o.generate_checking_report(self)
        return report


def generate_checking_report(station):
    well = station.well
    pump = station.pump_type
    dpipe = station.d_pipe
    coll = station.collector
    pumpset = station.pump_set

    n_of_work_pumps = station.calc_number_of_pumps()
    n_of_res_pumps = station.reserve_pumps_number()

    start_flow = (
        station.inflow_max.value_liters + station.inflow_min.value_liters) / 2
    end_params = station.get_work_parameters(start_flow, station.ord_sw_off)

    report = {}

    report['1'] = 'POMPA   POMPA   POMPA   POMPA   POMPA   POMPA   POMPA\n\n'
    report['2'] = 'Liniowe ustawienie pomp w pompowni'  # słownik
    report['3'] = 'Liczba dobranych pomp roboczych .....n= {} szt.'.format(
        n_of_work_pumps)
    report['4'] = 'Liczba pomp rezerwowych.............nr= {} szt.'.format(
        n_of_res_pumps)
    report['5'] = 'Srednica kola opisujacego pompe.....Dn= {} [m]'.format(
        pump.contour.value)
    report['6'] = 'Srednica pompowni...................DN= {} [m]'.format(
        well.diameter.value)
    report['7'] = 'Minimalna srednica pompowni......DNmin= {} [m]'.format(
        round(well.minimal_diameter(
            n_of_work_pumps, n_of_res_pumps, station), 2))
    report['8'] = 'Pole poziomego przekroju pompowni....F= {} [m2]'.format(
        round(well.cross_sectional_area(), 2))
    report['9'] = 'Ilosc przewodow tlocznych (kolektor)... {} szt.'.format(
        coll.parallels.value)
    report['10'] = 'Dlugosc kolektora tlocznego..........L= {} [m]'.format(
        coll.length.value)
    report['11'] = 'Dlugosc przewodu w pompowni..........L= {} [m]'.format(
        dpipe.length.value)
    report['12'] = 'Srednica kolektora tlocznego........Dn= {} [mm]'.format(
        coll.diameter.value)
    report['13'] = 'Srednica przewodu w pompowni........Dn= {} [mm]'.format(
        dpipe.diameter.value)
    report['14'] = 'Chropowatosc kolektora tlocznego.....k= {} [mm]'.format(
        coll.roughness.value)
    report['15'] = 'Chropowatosc przewodu w pompowni.....k= {} [mm]'.format(
        dpipe.roughness.value)
    report['16'] = 'Doplyw do pomowni....Qmin= {}   Qmax= {} [l/s]'.format(
        station.inflow_min.value_liters, station.inflow_max.value_liters)
    report['17'] = 'Rzedna terenu.........................  {} [m]'.format(
        station.ord_terrain.value)
    report['18'] = 'Rzedna doplywu sciekow................  {} [m]'.format(
        station.ord_inlet.value)
    report['19'] = 'Rzedna wylotu sciekow /przejscie'
    report['21'] = 'osi rury przez sciane pompowni/.......  {} [m]'.format(
        station.ord_outlet.value)
    report['22'] = 'Rzedna najwyzszego pkt. na trasie.....  {} [m]'.format(
        station.ord_highest_point.value)
    report['23'] = 'Rzedna zwierciadla w zbiorniku górnym.  {} [m]'.format(
        station.ord_upper_level.value)
    report['24'] = 'Min. wysokosc sciekow w  pompowni.....  {} [m]'.format(
        station.minimal_sewage_level.value)
    report['25'] = 'Suma wsp. oporow miejsc. kolektora....  {} [-]'.format(
        sum(coll.resistance.values))
    report['26'] = 'Suma wsp. oporow miejsc. w pompowni...  {} [-]\n'.format(
        sum(dpipe.resistance.values))
    report['27'] = 'CHARAKTERYSTYKA ZASTOSOWANYCH POMP\n'
    report['30'] = pump.generate_pump_char_string()
    report['31'] = 'Rzedna dna pompowni...................  {}\t[m]'.format(
        station.ord_bottom.value)
    report['32'] = 'Rzedna wylaczenia sie pomp............  {}\t[m]'.format(
        station.ord_bottom.value + 0.3)
    report['33'] = 'Objetosc calkowita pompowni.........Vc= {}\t[m3]'.format(
        round(station.v_whole, 2))
    report['34'] = 'Objetosc uzyteczna pompowni.........Vu= {}\t[m3]'.format(
        round(station.v_useful, 2))
    report['35'] = 'Objetosc rezerwowa pompowni.........Vr= {}\t[m3]'.format(
        round(station.v_reserve, 2))
    report['36'] = 'Objetosc martwa pompowni............Vm= {}\t[m3]\n'.format(
        round(station.v_dead, 2))
    report['37'] = 'Vu/Vc = {}%'.format(
        round(100 * (station.v_useful / station.v_whole)), 2)
    report['38'] = 'Vr/Vu = {}%'.format(
        round(100 * (station.v_reserve / station.v_useful)), 2)
    report['39'] = 'Vr/Vc = {}%'.format(
        round(100 * (station.v_reserve / station.v_whole)), 2)
    report['40'] = 'Vm/Vc = {}%\n'.format(
        round(100 * (station.v_dead / station.v_whole)), 2)
    '''
    report['47'] = 'Parametry poczatkowe pracy zespolu pomp'
    report['48'] = 'w chwili wlaczenia pompy nr{}\n'.format()
    report['49'] = '-wys. lc. u wylotu pompy...........Hlc= {} [m]'.format()
    report['50'] = '-geometryczna wys. podnoszenia.......H= {} [m]'.format()
    report['51'] = '-wydatek.............................Q= {} [l/s]'.format()
    report['52'] = '-predkosc w kolektorze tlocznym......v= {} [m/s]'.format()
    report['53'] = '-predkosc w przewodach w pompowni....v= {} [m/s]'.format()
    report['54'] = '-zapas wysokosci cisnienia..........dh= {} [m sł.wody]\n'.format()
    '''
    report['55'] = 'Parametry koncowe pracy zespolu pomp\n'
    report['56'] = '-wys. lc. u wylotu pompy...........Hlc= {} [m]'.format(
        end_params[0])
    report['57'] = '-geometryczna wys. podnoszenia.......H= {} [m]'.format(
        end_params[1])
    report['58'] = '-wydatek.............................Q= {} [l/s]'.format(
        end_params[2])
    report['59'] = '-predkosc w kolektorze tlocznym......v= {} [m/s]'.format(
        end_params[3])
    report['60'] = '-predkosc w przewodach w pompowni....v= {} [m/s]'.format(
        end_params[4])
    report['61'] = '-doplyw najniekorzystniejszy....Qdop=   {} [l/s]'.format(2)
    report['62'] = 'Zakres pracy pomp /maksymalna sprawnosc/'
    # report['63'] = 'Q1= {} [l/s]    Q2= {} [l/s]'.format()
    '''
    for pump in range(n_of_work_pumps):
        line = str(41 + pump)
        report[line] = pumpset.pumps[pump].report
    '''
    string_report = ''
    for i in report:
        log.debug('line {}: {}'.format(i, report[i]))
        if report[i] is not None:
            string_report += report[i]
            string_report += '\n'
    return string_report


class Report():

    # UWAGA - Do uzupełnienia argument dla minimalnej średnicy pompowni

    def __init__(self, station):
        self.station = station
        self.content = {}
        self.content['1'] = 'POMPA   POMPA   POMPA   POMPA   POMPA   POMPA   POMPA\n\n'
        self.content['2'] = self.write_conf(station.well.config.value)
        self.content['3'] = 'Liczba dobranych pomp roboczych .....n= {} szt.'.format(station.n_of_pumps)
        self.content['4'] = 'Liczba pomp rezerwowych.............nr= {} szt.'.format("station.n_of_res_pumps")
        self.content['5'] = 'Srednica kola opisujacego pompe.....Dn= {} [m]'.format(station.pump.contour.value)
        self.content['6'] = 'Srednica pompowni...................DN= {} [m]'.format(station.well.diameter.value)
        self.content['7'] = 'Minimalna srednica pompowni......DNmin= {} [m]'.format("%0.2f" % station.well.minimal_diameter(3, station))
        self.content['8'] = 'Pole poziomego przekroju pompowni....F= {} [m2]'.format(station.well.area)
        self.content['9'] = 'Ilosc przewodow tlocznych (kolektor)... {} szt.'.format(station.out_pipe.parallels.value)
        self.content['10'] = 'Dlugosc kolektora tlocznego..........L= {} [m]'.format(station.out_pipe.length.value)
        self.content['11'] = 'Dlugosc przewodu w pompowni..........L= {} [m]'.format(station.ins_pipe.length.value)
        self.content['12'] = 'Srednica kolektora tlocznego........Dn= {} [mm]'.format(station.out_pipe.diameter.value)
        self.content['13'] = 'Srednica przewodu w pompowni........Dn= {} [mm]'.format(station.ins_pipe.diameter.value)
        self.content['14'] = 'Chropowatosc kolektora tlocznego.....k= {} [mm]'.format(station.out_pipe.roughness.value)
        self.content['15'] = 'Chropowatosc przewodu w pompowni.....k= {} [mm]'.format(station.ins_pipe.roughness.value)
        self.content['16'] = 'Doplyw do pomowni....Qmin= {}   Qmax= {} [l/s]'.format(station.inflow_min.v_lps, station.inflow_max.v_lps)
        self.content['17'] = 'Rzedna terenu.........................  {} [m]'.format(station.ord_terrain.value)
        self.content['18'] = 'Rzedna doplywu sciekow................  {} [m]'.format(station.ord_inlet.value)
        self.content['19'] = 'Rzedna wylotu sciekow /przejscie'
        self.content['21'] = 'osi rury przez sciane pompowni/.......  {} [m]'.format(station.ord_outlet.value)
        self.content['22'] = 'Rzedna najwyzszego pkt. na trasie.....  {} [m]'.format(station.ord_highest_point.value)
        self.content['23'] = 'Rzedna zwierciadla w zbiorniku górnym.  {} [m]'.format(station.ord_upper_level.value)
        self.content['24'] = 'Min. wysokosc sciekow w  pompowni.....  {} [m]'.format(station.minimal_sewage_level.value)
        self.content['25'] = 'Suma wsp. oporow miejsc. kolektora....  {} [-]'.format(sum(station.out_pipe.resistance.values))
        self.content['26'] = 'Suma wsp. oporow miejsc. w pompowni...  {} [-]\n'.format(sum(station.ins_pipe.resistance.values))
        self.content['27'] = 'CHARAKTERYSTYKA ZASTOSOWANYCH POMP\n'
        self.content['30'] = self.station.pump.generate_pump_char_string()
        self.content['31'] = 'Rzedna dna pompowni...................  {}\t[m]'.format("%0.2f" % station.ord_bottom.value)
        self.content['32'] = 'Rzedna wylaczenia sie pomp............  {}\t[m]'.format("%0.2f" % station.ord_sw_off)
        self.content['33'] = 'Objetosc calkowita pompowni.........Vc= {}\t[m3]'.format("%0.2f" % station.v_whole)
        self.content['34'] = 'Objetosc uzyteczna pompowni.........Vu= {}\t[m3]'.format("%0.2f" % station.v_useful)
        self.content['35'] = 'Objetosc rezerwowa pompowni.........Vr= {}\t[m3]'.format("%0.2f" % station.v_reserve)
        self.content['36'] = 'Objetosc martwa pompowni............Vm= {}\t[m3]\n'.format("%0.2f" % station.v_dead)
        self.content['37'] = 'Vu/Vc = {}%'.format("%0.2f" % (100 * (station.v_useful / station.v_whole)))
        self.content['38'] = 'Vr/Vu = {}%'.format("%0.2f" % (100 * (station.v_reserve / station.v_useful)))
        self.content['39'] = 'Vr/Vc = {}%'.format("%0.2f" % (100 * (station.v_reserve / station.v_whole)))
        self.content['40'] = 'Vm/Vc = {}%\n'.format("%0.2f" % (100 * (station.v_dead / station.v_whole)))

        self.content['41'] = self.pump_report()

        self.print_rep()

    def write_conf(self, config):
        conf_dict = {'singlerow': 'Liniowe',
                     'optimal': 'Optymalne'}
        log.debug('config: {}'.format(config))
        log.debug('confdict[config]: {}'.format(conf_dict[config]))
        return '{} ustawienie pomp w pompowni'.format(conf_dict[config])

    def convert_to_string(self):
        string_report = ''
        for i in self.content:
            log.debug('line {}: {}'.format(i, self.content[i]))
            if self.content[i] is not None:
                string_report += self.content[i]
                string_report += '\n'
        return string_report

    def print_rep(self):
        self.string = self.convert_to_string()
        print(self.string)

    def pump_report(self):
        report = ''
        for pump in range(self.station.n_of_pumps):
            pump_no = pump + 1
            prms = self.station.work_parameters[str(pump_no)]
            report += 'PARAMETRY POMPY NR: {}\n\n'.format(pump_no)
            report += 'Rzeczywisty czas cyklu pompy.......T= {}\t[s]\n'.format(prms['times'][0])
            report += 'Rzeczywisty czas postoju pompy....Tp= {}\t[s]\n'.format(prms['times'][1])
            report += 'Rzeczywisty czas pracy pompy......Tr= {}\t[s]\n'.format(prms['times'][2])
            report += 'Obj. uzyt. wyzn. przez pompe......Vu= {}\t[m3]\n'.format(prms['vol_a'])
            report += 'Rzedna wlaczenia pompy..............  {}\t[m]\n\n'.format("%0.2f" % prms['ord_sw_on'])
            report += 'Parametry poczatkowe pracy zespolu pomp\nw chwili wlaczenia pompy nr{}\n\n'.format(pump_no)
            report += '-wys. lc. u wylotu pompy.........Hlc= {}\t[m]\n'.format("%0.2f" % prms['start'][0])
            report += '-geometryczna wys. podnoszenia.....H= {}\t[m]\n'.format("%0.2f" % prms['start'][1])
            report += '-wydatek...........................Q= {}\t[l/s]\n'.format("%0.2f" % prms['start'][2].v_lps)
            report += '-predkosc w kolektorze tlocznym....v= {}\t[m/s]\n'.format("%0.2f" % prms['start'][3])
            report += '-predkosc w przewodach w pompowni..v= {}\t[m/s]\n'.format("%0.2f" % prms['start'][4])
            report += '-zapas wysokosci cisnienia.....dh=  {}\t[m sl.wody]\n\n'.format('??')
            report += 'Parametry koncowe pracy zespolu pomp\n\n'
            report += '-wys. lc. u wylotu pompy.........Hlc= {}\t[m]\n'.format("%0.2f" % prms['stop'][0])
            report += '-geometryczna wys. podnoszenia.....H= {}\t[m]\n'.format("%0.2f" % prms['stop'][1])
            report += '-wydatek...........................Q= {}\t[l/s]\n'.format("%0.2f" % prms['stop'][2].v_lps)
            report += '-predkosc w kolektorze tlocznym....v= {}\t[m/s]\n'.format("%0.2f" % prms['stop'][3])
            report += '-predkosc w przewodach w pompowni..v= {}\t[m/s]\n'.format("%0.2f" % prms['stop'][4])
            report += '-doplyw najniekorzystniejszy....Qdop= {}\t[m]\n'.format("%0.2f" % prms['worst_infl'].v_lps)
            report += 'Zakres pracy pomp /maksymalna sprawnosc/\n'
            report += 'Q1=  {} [l/s]    Q2=  {} [l/s]\n'.format(
                (pump_no) * self.station.pump.efficiency_from.v_lps,
                (pump_no) * self.station.pump.efficiency_to.v_lps)

        report += '\n\n'
        return report
