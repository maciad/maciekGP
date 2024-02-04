from random import Random
from ProgramRunContext import ProgramRunContext
import math
import operator
from copy import deepcopy
from datetime import datetime
# from evolution.EvolutionHistory import EvolutionHistory, Generation
from ProgramGenerator.TreeGenerator import *
from Crossover import Crossover
# from TestSets.gradingFunctions import GradingFunction


class Evolution:
    random = Random()
    POPULATION_SIZE = 1000

    @staticmethod
    def perform_evolution(test_set, max_generations=50):
        max_execution_time = test_set.config.max_execution_time
        # start_time = datetime.now()
        print("starting evolution for test set:" + test_set.name)

        # eh = EvolutionHistory()
        current_generation_index = 1

        # create initial population
        # generation = Generation()
        population = []
        for i in range(Evolution.POPULATION_SIZE):
            population.append(generate_program_node_count(12))  # TODO: change to config

        # evaluate initial population
        evaluated_population = Evolution.evaluate_population(population, test_set, test_set.grading_function, test_set.config.max_execution_time)

        while current_generation_index < max_generations:
            # best_fitness = min(evaluated_population.values())
            # best_program = list(evaluated_population.keys())[list(evaluated_population.values()).index(best_fitness)]
            best_program, best_fitness = min(evaluated_population.items(), key=operator.itemgetter(1))
            avg_fitness = sum(evaluated_population.values()) / len(evaluated_population)
            print("Generation: " + str(current_generation_index) + " best fitness: " + str(best_fitness), "avg fitness: " + str(avg_fitness))
            if best_fitness <= test_set.threshold:
                break

            new_population = []
            # add 5% of the best programs to the new population
            best_programs = sorted(evaluated_population, key=evaluated_population.get)
            for i in range(int(Evolution.POPULATION_SIZE * 0.05)):
                new_population.append(best_programs[i])

            while len(new_population) < Evolution.POPULATION_SIZE:
                # mutation
                if Evolution.random.random() < test_set.config.mutation_chance:
                    program = Evolution.random.choice(population)
                    while not program.can_be_mutated():
                        program = Evolution.random.choice(population)
                    new_program = deepcopy(program)  # TODO: check for possible problems with deepcopy
                    type_to_mutate = type(Evolution.random.choice(new_program.mutables))
                    new_program.mutate(type_to_mutate)
                    new_population.append(new_program)
                # crossover
                else:
                    success = False
                    while not success:
                        parent1 = Evolution.tournament_selection(evaluated_population)
                        parent2 = Evolution.tournament_selection(evaluated_population)
                        if parent1 != parent2:
                            new_program_1, new_program_2 = Crossover.cross_programs(parent1, parent2, test_set.config)
                            if new_program_1 is not None and new_program_2 is not None:
                                new_population.append(new_program_1)
                                new_population.append(new_program_2)
                                success = True

            population = new_population
            current_generation_index += 1

            # evaluate new population
            evaluated_population = Evolution.evaluate_population(population, test_set, test_set.grading_function, test_set.config.max_execution_time)
            best_program, best_fitness = min(evaluated_population.items(), key=operator.itemgetter(1))
            avg_fitness = sum(evaluated_population.values()) / len(evaluated_population)
            print("================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================")
            print("Generation: " + str(current_generation_index) + " best fitness: " + str(best_fitness), "avg fitness: " + str(avg_fitness))

        print(best_program)
        return best_program

    @staticmethod
    def tournament_selection(evaluated_population, tournament_size=5):
        target = Evolution.random.choice(list(evaluated_population.keys()))
        for i in range(tournament_size - 1):
            competitor = Evolution.random.choice(list(evaluated_population.keys()))
            if target == None or evaluated_population[competitor] < evaluated_population[target]:
                target = competitor
        return target

    @staticmethod
    def evaluate_population(population, test_set, grading_function, max_actions):
        result = {}
        for program in population:
            grades = []
            for test_case in test_set.test_cases:
                program_run_context = ProgramRunContext()
                program_run_context.input = test_case.input.copy()
                program_run_context.max_executed_actions = max_actions
                program.invoke(program_run_context)
                if not program_run_context.has_timed_out():
                    grades.append(grading_function(test_case, program_run_context))
                else:
                    grades.append(math.inf)
                    break
                result[program] = sum(grades) / len(grades)  # TODO: zastanowic sie czy to jest poprawne
        return result

