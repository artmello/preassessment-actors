#!/usr/bin/env python
""" Sample script to execute some PreAssessment scripts """
import logging
import os
from collections import deque, namedtuple
from shutil import rmtree

from snactor.loader import load, load_schemas, validate_actor_types, get_actor


def default_writer(out, entry):
    """ Default actor output writer """
    out.write("{}\n".format(entry))


def pkg_writer(out, entry):
    """ Actor's pkg output writer """
    out.write("{}\t{}\t{}\n".format(entry['name'], entry['vendor'], entry['signature']))


def main():
    """ Run all actors """
    logging.basicConfig(format='%(asctime)s: %(message)s',
                        level=logging.WARNING)

    Actor = namedtuple('Actor', ['name', 'desc', 'deps', 'logfile', 'writer'])

    actors = [
        Actor('rpm_qa', 'All installed packages', [], 'rpm_qa.log', pkg_writer),
        Actor('rpm_va', 'All changed files', [], 'rpm_va.log', default_writer),
        Actor('rpm_qal', 'All installed files', [], 'rpmtrackedfiles.log', default_writer),
        Actor('getent_passwd', 'All users', [], 'passwd.log', default_writer),
        Actor('getent_group', 'All groups', [], 'group.log', default_writer),
        Actor('chkconfig_list', 'Service statuses', [], 'chkconfig.log', default_writer),
        Actor('local_file_systems', 'All local file systems', [], None, None),
        Actor('redhat_signed_pkgs', 'Red hat signed pkgs', ['rpm_qa'], 'rpm_rhsigned.log', pkg_writer),
        Actor('changed_config', 'Changed config files', ['rpm_va'], 'rpm_etc_Va.log', default_writer),
        Actor('all_files', 'All local files', ['local_file_systems'], 'allmyfiles.log', default_writer),
        Actor('all_executables', 'All executable files', ['local_file_systems'], 'executable.log', default_writer)]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    actors_dir = os.path.join(base_dir, 'actors')
    schemas_dir = os.path.join(base_dir, 'schemas')
    logs_dir = os.path.join(base_dir, 'logs')

    """ Loading actors """
    logging.warning("[loading] actors: %s ...", actors_dir)
    load(actors_dir)
    logging.warning("[loading] schemas: %s ...", schemas_dir)
    load_schemas(schemas_dir)
    logging.warning("[validating] actors/schemas ...")
    validate_actor_types()

    """ Running actors """
    done = []
    pending = deque(actors)
    data = {}
    while pending:
        actor = pending.popleft()
        if not set(actor.deps).issubset(set(done)):
            pending.append(actor)
            continue

        logging.warning("[running] (%s) %s ...", os.path.join(actors_dir, actor.name), actor.desc)
        get_actor(actor.name).execute(data)
        done.append(actor.name)

    """ Saving actors output"""
    if os.path.exists(logs_dir):
        rmtree(logs_dir)

    os.makedirs(logs_dir)

    with_log = [a for a in actors if a.logfile]
    for actor in with_log:
        logfile = os.path.join(logs_dir, actor.logfile)
        logging.warning("[writing] %s ...", logfile)
        with open(logfile, 'w') as log:
            for entry in data[actor.name]['entries']:
                actor.writer(log, entry)


if __name__ == '__main__':
    main()
