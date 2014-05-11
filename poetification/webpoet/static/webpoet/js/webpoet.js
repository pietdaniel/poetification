$(document).ready(function(){
	console.log("Hack Beanpot for the win");

	list = ['ABBREVIATION', 'ABOMINATION', 'ACCELERATION', 'ACCOMMODATION', 'ACCREDITATION', 'ACCUMULATION', 'ACIDIFICATION', 'ADJUDICATION', 'ADMINISTRATION', 'ADULTERATION', 'AFFILIATION', 'AGGLOMERATION', 'ALIENATION', 'ALLEVIATION', 'ALPHABETIZATIONBINARY', 'AMALGAMATION', 'AMELIORATION', 'AMORTIZATION', 'AMPLIFICATION', 'ANNIHILATION', 'ANTICIPATION', 'APPLICATION', 'APPLICATION', 'APPRECIATION', 'APPROPRIATION', 'APPROXIMATION', 'ARGUMENTATION', 'ARTICULATION', 'ASSASSINATION', 'ASSIMILATION', 'BASSOCIATION', 'BAUTHENTICATION', 'BAUTHORIZATION', 'BALKANIZATION', 'CANNIBALIZATION', 'CANONIZATION', 'CAPITALIZATION', 'CAPITULATION', 'CATEGORIZATION', 'CAUTERIZATION', 'CENTRALIZATION', 'CERTIFICATION', 'CHARACTERIZATION', 'CHRISTIANIZATION', 'CIVILIZATION', 'CLADIFICATION', 'CLARIFICATION', 'CLASSIFICATION', 'COAGULATION', 'CODIFICATION', 'COGENERATION', 'COHABITATION', 'COLLABORATION', 'COLLECTIVIZATION', 'COLONIZATION', 'COLORIZATION', 'COMMEMORATION', 'COMMERCIALIZATION', 'COMMUNICATION', 'COMMUNIZATION', 'COMPUTERIZATION', 'CONCATENATION', 'CONCILIATION', 'CONFABULATION', 'CONFEDERATION', 'CONFIGURATION', 'CONGLOMERATION', 'CONGRATULATION', 'CONSERVATION', 'CONSERVATION', 'CONSIDERATION', 'CONSOLIDATION', 'CONTAMINATION', 'CONTINUATION', 'COOPERATION', 'COORDINATION', 'CORPORATION', 'CORPORATION', 'CORPORATION', 'CORRELATION', 'CORRELATION', 'CORROBORATION', 'DECAFFEINATION', 'DECAPITATION', 'DECELERATION', 'DECORATION', 'DEFORESTATION', 'DEGENERATION', 'DEIFICATION', 'DELIBERATION', 'DELINEATION', 'DEMODULATION', 'DEMONIZATION', 'DENOMINATION', 'DENUNCIATION', 'DEPRECIATION', 'DEREGULATION', 'DESALINATION', 'DESEGREGATION', 'DISINCLINATION', 'DISINFORMATION', 'DISINTEGRATION', 'DISSEMINATION', 'DISSOCIATION', 'DIVINATION', 'DOCUMENTATION', 'DOMESTICATION', 'DRAMATIZATION', 'ECHOLOCATION', 'EJACULATION', 'ELABORATION', 'ELIMINATION', 'EMANCIPATION', 'ENUMERATION', 'EQUALIZATION', 'EQUIVOCATION', 'ERADICATION', 'EVACUATION', 'EVALUATION', 'EVAPORATION', 'EXACERBATION', 'EXAGGERATION', 'EXAMINATION', 'EXASPERATION', 'EXFOLIATION', 'EXHILARATION', 'EXPATRIATION', 'EXPROPRIATION', 'EXTERMINATION', 'EXTRAPOLATION', 'FACILITATION', 'FALSIFICATION', 'FERTILIZATION', 'FINLANDIZATION', 'FORMATION', 'FORTIFICATION', 'FOUNDATION', 'GASIFICATION', 'GENERATION', 'GENETIZATION', 'GENTRIFICATION', 'GLOBALIZATION', 'GLORIFICATION', 'GRATIFICATION', 'HALLUCINATION', 'HARMONIZATION', 'HUMILIATION', 'HYBRIDIZATION', 'HYDROGENATION', 'HYPERINFLATION', 'ILLUMINATION', 'IMAGINATION', 'IMMUNIZATION', 'IMPERSONATION', 'IMPLEMENTATION', 'IMPROVISATION', 'INACTIVATION', 'INAUGURATION', 'INCARCERATION', 'INCORPORATION', 'INCRIMINATION', 'INDOCTRINATION', 'INFATUATION', 'INFLATION', 'INHABITATION', 'INITIATION', 'INNOCULATION', 'INOCULATION', 'INSEMINATION', 'INSINUATION', 'INSTANTIATION', 'INSTRUMENTATION', 'INTERPRETATION', 'INTERROGATION', 'INTIMIDATION', 'INTOXICATION', 'INVALIDATION', 'INVESTIGATION', 'IONIZATION', 'IRRADIATION', 'ISLAMIZATION', 'MAGNIFICATION', 'MANIFESTATION', 'MANIPULATION', 'MAXIMIZATION', 'MECHANIZATION', 'MISALLOCATION', 'MISAPPLICATION', 'MISCALCULATION', 'MISINFORMATION', 'MOBILIZATION', 'MODERNIZATION', 'MODIFICATION', 'MODULATION', 'MODULATION', 'MULTIPLICATION', 'MUMMIFICATION', 'NEGOTIATION', 'NEUTRALIZATION', 'NORMALIZATION', 'NOTIFICATION', 'NULLIFICATION', 'OBLITERATION', 'OPERATION', 'OPTIMIZATION', 'ORGANISATION', 'ORGANIZATION', 'ORIENTATION', 'ORIGINATION', 'ORNAMENTATION', 'OSSIFICATION', 'PACIFICATION', 'PANELIZATION', 'PARTICIPATION', 'PASTEURIZATION', 'PERPETUATION', 'POLARIZATION', 'PONTIFICATION', 'PRECIPITATION', 'PREDESTINATION', 'PREFABRICATION', 'PREMEDITATION', 'PREOCCUPATION', 'PRESSURIZATION', 'PREVARICATION', 'PRIVATISATION', 'PRIVATIZATION', 'PROCRASTINATION', 'PROGNOSTICATION', 'PROLIFERATION', 'PRONUNCIATION', 'PROSTRATION', 'PURIFICATION', 'QUALIFICATION', 'QUANTIFICATION', 'QUOTATION', 'RAMIFICATION', 'RATIFICATION', 'REAFFIRMATION', 'REALLOCATION', 'RECALCULATION', 'RECOMMENDATION', 'RECONFIRMATION', 'RECRIMINATION', 'RECTIFICATION', 'RECUPERATION', 'REDECORATION', 'REDEDICATION', 'REFORESTATION', 'REFRIGERATION', 'REGENERATION', 'REGIMENTATION', 'REINCARNATION', 'REITERATION', 'REJUVENATION', 'REMEDIATION', 'REMUNERATION', 'RENOMINATION', 'RENUNCIATION', 'REPATRIATION', 'REPRESENTATION', 'REPUDIATION', 'REREGULATION', 'RESUSCITATION', 'RETALIATION', 'REVALUATION', 'REVERBERATION', 'RUSSIFICATION', 'SANCTIFICATION', 'SAUDIIZATION', 'SEDIMENTATION', 'SEGREGATION', 'SENSATION', 'SENSATION', 'SEPARATION', 'SIMPLIFICATION', 'SOCIALIZATION', 'SOLICITATION', 'SOPHISTICATION', 'SPECIALIZATION', 'SPECIFICATION', 'STABILIZATION', 'STALINIZATION', 'STANDARDIZATION', 'STERILIZATION', 'SUBORDINATION', 'SUBSIDIZATION', 'SUBSTANTIATION', 'SYNCHRONIZATION', 'TABLOIDIZATION', 'TRANSLATION', 'TRIANGULATION', 'UNIFICATION', 'UNIONIZATION', 'URBANIZATION', 'UTILIZATION', 'VAPORIZATION', 'VERIFICATION', 'VICTIMIZATION', 'VILIFICATION', 'VISUALIZATION', 'VULGARIZATION', 'WESTERNIZATION'];

	setInterval(function(){
		if (list.length>250) {
			$('#home_title').html(list.pop());
		} else {
			$('#home_title').html("RHYMING STAT.US");
			clearInterval();
			$('#home_title').animate({
				letterSpacing: "20px",
			}, {
				easing: "easeOutQuint",
				duration: 10000,
			});
		}
	}, 25);
});


